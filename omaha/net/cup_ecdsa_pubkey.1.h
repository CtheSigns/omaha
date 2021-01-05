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
0x50, 0x1b, 0x1e, 0xba, 0xb1, 0x72, 0x5a, 0x2b,
0x8b, 0x7e, 0x78, 0xe5, 0xbb, 0xf1, 0x24, 0x22,
0xe8, 0xc4, 0xd0, 0xcc, 0xc8, 0x54, 0xa0, 0x26,
0x3e, 0x14, 0xdd, 0xd7, 0xb0, 0x12, 0x71, 0x27,
0xae, 0xd3, 0x5c, 0x09, 0xc0, 0x61, 0x34, 0xa6,
0x07, 0x1e, 0xfb, 0x3a, 0x5e, 0x41, 0xf1, 0x12,
0x5e, 0x3c, 0xe9, 0x23, 0x97, 0x10, 0x24, 0x44,
0x4a, 0x37, 0x3d, 0x57, 0x31, 0x3e, 0x95, 0x2d};

