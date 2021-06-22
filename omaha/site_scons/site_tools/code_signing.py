# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================

"""Code signing build tool.

This module sets up code signing.
It is used as follows:
  env = Environment(tools = ["code_signing"])
To sign an EXE/DLL do:
  env.SignedBinary('hello_signed.exe', 'hello.exe',
                   CERTIFICATE_FILE='bob.pfx',
                   CERTIFICATE_PASSWORD='123',
                   TIMESTAMP_SERVER='')
If no certificate file is specified, copying instead of signing will occur.
If an empty timestamp server string is specified, there will be no timestamp.
"""

import optparse
from SCons.compat._scons_optparse import OptionConflictError
import SCons.Script


def generate(env):
  # NOTE: SCons requires the use of this name, which fails gpylint.
  """SCons entry point for this tool."""

  try:
    SCons.Script.AddOption('--certificate-name',
                           dest='certificate_name',
                           help='select which certificate to use')
    SCons.Script.Help(
        '  --certificate-name <NAME>   select which signing certificate to use')
  except (OptionConflictError, optparse.OptionConflictError):
    # This gets catch to prevent duplicate help being added for this option
    # for each build type.
    pass

  env.SetDefault(
      # Path to Microsoft signtool.exe
      SIGNTOOL='"$THIRD_PARTY/code_signing/signtool.exe"',
      # No certificate by default.
      CERTIFICATE_PATH='',
      # No sha1 certificate by default.
      SHA1_CERTIFICATE_PATH='',
      # No sha256 certificate by default.
      SHA2_CERTIFICATE_PATH='',
      # No certificate password by default.
      CERTIFICATE_PASSWORD='',
      # The default timestamp server.
      TIMESTAMP_SERVER='http://timestamp.comodoca.com/authenticode',
      # The default timestamp server when dual-signing.
      SHA1_TIMESTAMP_SERVER='http://timestamp.comodoca.com/authenticode',
      # The default timestamp server for sha256 timestamps.
      SHA2_TIMESTAMP_SERVER='http://timestamp.comodoca.com/rfc3161',
      # The default certificate store.
      CERTIFICATE_STORE='my',
      # Set the certificate name from the command line.
      CERTIFICATE_NAME=SCons.Script.GetOption('certificate_name'),
      # The name (substring) of the certificate issuer, when needed to
      # differentiate between multiple certificates.
      SHA1_CERTIFICATE_ISSUER='Verisign',
      SHA2_CERTIFICATE_ISSUER='Symantec',
      # Or differentiate based on the cert's hash.
      CERTIFICATE_HASH='5A9272CE76A9415A4A3A5002A2589A049312AA40',
      SHA1_CERTIFICATE_HASH='',
      SHA2_CERTIFICATE_HASH='',
  )

  # Setup Builder for Signing
  env['BUILDERS']['SignedBinary'] = SCons.Script.Builder(
      generator=SignedBinaryGenerator,
      emitter=SignedBinaryEmitter)
  env['BUILDERS']['DualSignedBinary'] = SCons.Script.Builder(
      generator=DualSignedBinaryGenerator,
      emitter=SignedBinaryEmitter)


def SignedBinaryEmitter(target, source, env):
  """Add the signing certificate (if any) to the source dependencies."""
  if env.subst('$CERTIFICATE_PATH'):
    source.append(env.subst('$CERTIFICATE_PATH'))
  return target, source


def SignedBinaryGenerator(source, target, env, for_signature):
  """A builder generator for code signing."""
  source = source                # Silence gpylint.
  target = target                # Silence gpylint.
  for_signature = for_signature  # Silence gpylint.

  # Alway copy and make writable.
  commands = [
      SCons.Script.Copy('$TARGET', '$SOURCE'),
      SCons.Script.Chmod('$TARGET', 0755),
  ]

  signing_cmd = '$SIGNTOOL sign /tr http://timestamp.comodoca.com /td sha1 /fd sha1 /a $TARGET'
  commands.append(signing_cmd)

  return commands

def DualSignedBinaryGenerator(source, target, env, for_signature):
  """A builder generator for code signing with two certs."""
  source = source                # Silence gpylint.
  target = target                # Silence gpylint.
  for_signature = for_signature  # Silence gpylint.

  # Alway copy and make writable.
  commands = [
      SCons.Script.Copy('$TARGET', '$SOURCE'),
      SCons.Script.Chmod('$TARGET', 0755),
  ]
    
  sha1_signing_cmd = '$SIGNTOOL sign /v /tr http://timestamp.comodoca.com /td sha1 /fd sha1 /a $TARGET'
  commands.append(sha1_signing_cmd)

  sha2_signing_cmd = '$SIGNTOOL sign /v /tr "http://timestamp.comodoca.com" /td "SHA256" /as /fd "SHA256" "$TARGET"'
  commands.append(sha2_signing_cmd)


  return commands
