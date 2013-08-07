# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

INCLUDES = [
    '#include "openssl/evp.h"',
]

FUNCTIONS = [
    'const EVP_CIPHER *EVP_enc_null(void);',
    'const EVP_CIPHER *EVP_des_ecb(void);',
    'const EVP_CIPHER *EVP_des_ede(void);',
    'const EVP_CIPHER *EVP_des_ede3(void);',
    'const EVP_CIPHER *EVP_des_ede_ecb(void);',
    'const EVP_CIPHER *EVP_des_ede3_ecb(void);',
    'const EVP_CIPHER *EVP_des_cfb64(void);',
    'const EVP_CIPHER *EVP_des_cfb1(void);',
    'const EVP_CIPHER *EVP_des_cfb8(void);',
    'const EVP_CIPHER *EVP_des_ede_cfb64(void);',
    'const EVP_CIPHER *EVP_des_ede3_cfb64(void);',
    'const EVP_CIPHER *EVP_des_ede3_cfb1(void);',
    'const EVP_CIPHER *EVP_des_ede3_cfb8(void);',
    'const EVP_CIPHER *EVP_des_ofb(void);',
    'const EVP_CIPHER *EVP_des_ede_ofb(void);',
    'const EVP_CIPHER *EVP_des_ede3_ofb(void);',
    'const EVP_CIPHER *EVP_des_cbc(void);',
    'const EVP_CIPHER *EVP_des_ede_cbc(void);',
    'const EVP_CIPHER *EVP_des_ede3_cbc(void);',
    'const EVP_CIPHER *EVP_desx_cbc(void);',
    'const EVP_CIPHER *EVP_rc4(void);',
    'const EVP_CIPHER *EVP_rc4_40(void);',
    'const EVP_CIPHER *EVP_rc2_ecb(void);',
    'const EVP_CIPHER *EVP_rc2_cbc(void);',
    'const EVP_CIPHER *EVP_rc2_40_cbc(void);',
    'const EVP_CIPHER *EVP_rc2_64_cbc(void);',
    'const EVP_CIPHER *EVP_rc2_cfb64(void);',
    'const EVP_CIPHER *EVP_rc2_ofb(void);',
    'const EVP_CIPHER *EVP_bf_ecb(void);',
    'const EVP_CIPHER *EVP_bf_cbc(void);',
    'const EVP_CIPHER *EVP_bf_cfb64(void);',
    'const EVP_CIPHER *EVP_bf_ofb(void);',
    'const EVP_CIPHER *EVP_cast5_ecb(void);',
    'const EVP_CIPHER *EVP_cast5_cbc(void);',
    'const EVP_CIPHER *EVP_cast5_cfb64(void);',
    'const EVP_CIPHER *EVP_cast5_ofb(void);',
    'const EVP_CIPHER *EVP_aes_128_ecb(void);',
    'const EVP_CIPHER *EVP_aes_128_cbc(void);',
    'const EVP_CIPHER *EVP_aes_128_cfb1(void);',
    'const EVP_CIPHER *EVP_aes_128_cfb8(void);',
    'const EVP_CIPHER *EVP_aes_128_cfb128(void);',
    'const EVP_CIPHER *EVP_aes_128_ofb(void);',
    'const EVP_CIPHER *EVP_aes_192_ecb(void);',
    'const EVP_CIPHER *EVP_aes_192_cbc(void);',
    'const EVP_CIPHER *EVP_aes_192_cfb1(void);',
    'const EVP_CIPHER *EVP_aes_192_cfb8(void);',
    'const EVP_CIPHER *EVP_aes_192_cfb128(void);',
    'const EVP_CIPHER *EVP_aes_192_ofb(void);',
    'const EVP_CIPHER *EVP_aes_256_ecb(void);',
    'const EVP_CIPHER *EVP_aes_256_cbc(void);',
    'const EVP_CIPHER *EVP_aes_256_cfb1(void);',
    'const EVP_CIPHER *EVP_aes_256_cfb8(void);',
    'const EVP_CIPHER *EVP_aes_256_cfb128(void);',
    'const EVP_CIPHER *EVP_aes_256_ofb(void);',
]
