// Copyright 2020 Google Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// ========================================================================
//
// CUP-ECDSA public keys consist of a byte array, 66 bytes long, containing:
// * The key ID (one byte)
// * The public key in X9.62 uncompressed encoding (65 bytes):
//     * Uncompressed header byte (0x04)
//     * Gx coordinate (256-bit integer, big-endian)
//     * Gy coordinate (256-bit integer, big-endian)
{0x01,
0x04,
0x4c, 0x92, 0x85, 0x2a, 0x33, 0xe7, 0x2c, 0xe5,
0x3d, 0x11, 0x4e, 0xf4, 0x0a, 0xea, 0x89, 0xe7,
0x8f, 0xca, 0xb4, 0x03, 0xd2, 0xbb, 0xde, 0x10,
0xcb, 0x77, 0x2d, 0xca, 0xd2, 0x70, 0xb3, 0xfd,
0xc2, 0xb2, 0x93, 0x2b, 0x7a, 0x76, 0x71, 0x44,
0xc8, 0x35, 0xd4, 0x74, 0xe5, 0x8c, 0xd3, 0x7b,
0x84, 0x8d, 0xa5, 0x78, 0xfb, 0x77, 0x65, 0xed,
0xcf, 0xa1, 0x78, 0xc2, 0xec, 0xa1, 0x2e, 0xf3};
