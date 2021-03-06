# DO NOT MODIFY THIS FILE!  It was automatically generated.
# -*- coding: utf-8 -*-

# Conversion between different charsets, surfaces and structures.
# Copyright © 1993, 1997, 1999, 2002, 2004 Free Software Foundation, Inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1993.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.

# This library is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with the `recode' Library; see the file `COPYING.LIB'.
# If not, write to the Free Software Foundation, Inc., 59 Temple Place -
# Suite 330, Boston, MA 02111-1307, USA.

import recode

declares = [
    ('ascii', '646', 'ansi_x3.4_1968', 'ansi_x3.4_1986', 'ansi_x3_4_1968', 'cp367', 'csascii', 'ibm367', 'iso646_us', 'iso_646.irv_1991', 'iso_ir_6', 'us', 'us_ascii'),
    ('base64_codec', 'base64', 'base_64'),
    ('big5', 'big5_tw', 'csbig5'),
    ('big5hkscs', 'hkscs'),
    ('bz2_codec', 'bz2'),
    ('cp037', '037', 'csibm037', 'ebcdic_cp_ca', 'ebcdic_cp_nl', 'ebcdic_cp_us', 'ebcdic_cp_wt', 'ibm037', 'ibm039'),
    'cp1006',
    ('cp1026', '1026', 'csibm1026', 'ibm1026'),
    ('cp1140', '1140', 'ibm1140'),
    ('cp1250', '1250', 'windows_1250'),
    ('cp1251', '1251', 'windows_1251'),
    ('cp1252', '1252', 'windows_1252'),
    ('cp1253', '1253', 'windows_1253'),
    ('cp1254', '1254', 'windows_1254'),
    ('cp1255', '1255', 'windows_1255'),
    ('cp1256', '1256', 'windows_1256'),
    ('cp1257', '1257', 'windows_1257'),
    ('cp1258', '1258', 'windows_1258'),
    ('cp424', '424', 'csibm424', 'ebcdic_cp_he', 'ibm424'),
    ('cp437', '437', 'cspc8codepage437', 'ibm437'),
    ('cp500', '500', 'csibm500', 'ebcdic_cp_be', 'ebcdic_cp_ch', 'ibm500'),
    'cp720',
    'cp737',
    ('cp775', '775', 'cspc775baltic', 'ibm775'),
    ('cp850', '850', 'cspc850multilingual', 'ibm850'),
    ('cp852', '852', 'cspcp852', 'ibm852'),
    ('cp855', '855', 'csibm855', 'ibm855'),
    'cp856',
    ('cp857', '857', 'csibm857', 'ibm857'),
    ('cp858', '858', 'csibm858', 'ibm858'),
    ('cp860', '860', 'csibm860', 'ibm860'),
    ('cp861', '861', 'cp_is', 'csibm861', 'ibm861'),
    ('cp862', '862', 'cspc862latinhebrew', 'ibm862'),
    ('cp863', '863', 'csibm863', 'ibm863'),
    ('cp864', '864', 'csibm864', 'ibm864'),
    ('cp865', '865', 'csibm865', 'ibm865'),
    ('cp866', '866', 'csibm866', 'ibm866'),
    ('cp869', '869', 'cp_gr', 'csibm869', 'ibm869'),
    'cp874',
    'cp875',
    ('cp932', '932', 'ms932', 'ms_kanji', 'mskanji'),
    ('cp949', '949', 'ms949', 'uhc'),
    ('cp950', '950', 'ms950'),
    ('euc_jis_2004', 'jisx0213'),
    'euc_jisx0213',
    ('euc_jp', 'u_jis', 'ujis'),
    ('euc_kr', 'korean', 'ks_c_5601', 'ks_c_5601_1987', 'ks_x_1001', 'ksc5601', 'ksx1001'),
    ('gb18030', 'gb18030_2000'),
    ('gb2312', 'chinese', 'csiso58gb231280', 'euc_cn', 'euccn', 'eucgb2312_cn', 'gb2312_1980', 'gb2312_80', 'iso_ir_58'),
    ('gbk', '936', 'cp936', 'ms936'),
    ('hex_codec', 'hex'),
    ('hp_roman8', 'csHPRoman8', 'r8', 'roman8'),
    ('hz', 'hz_gb', 'hz_gb_2312', 'hzgb'),
    'idna',
    ('iso2022_jp', 'csiso2022jp'),
    'iso2022_jp_1',
    'iso2022_jp_2',
    'iso2022_jp_2004',
    'iso2022_jp_3',
    'iso2022_jp_ext',
    ('iso2022_kr', 'csiso2022kr'),
    ('iso8859_10', 'csisolatin6', 'iso_8859_10_1992', 'iso_ir_157', 'l6', 'latin6'),
    ('iso8859_11', 'iso_8859_11_2001', 'thai'),
    ('iso8859_13', 'l7', 'latin7'),
    ('iso8859_14', 'iso_8859_14_1998', 'iso_celtic', 'iso_ir_199', 'l8', 'latin8'),
    ('iso8859_15', 'l9', 'latin9'),
    ('iso8859_16', 'iso_8859_16_2001', 'iso_ir_226', 'l10', 'latin10'),
    ('iso8859_2', 'csisolatin2', 'iso_8859_2_1987', 'iso_ir_101', 'l2', 'latin2'),
    ('iso8859_3', 'csisolatin3', 'iso_8859_3_1988', 'iso_ir_109', 'l3', 'latin3'),
    ('iso8859_4', 'csisolatin4', 'iso_8859_4_1988', 'iso_ir_110', 'l4', 'latin4'),
    ('iso8859_5', 'csisolatincyrillic', 'cyrillic', 'iso_8859_5_1988', 'iso_ir_144'),
    ('iso8859_6', 'arabic', 'asmo_708', 'csisolatinarabic', 'ecma_114', 'iso_8859_6_1987', 'iso_ir_127'),
    ('iso8859_7', 'csisolatingreek', 'ecma_118', 'elot_928', 'greek', 'greek8', 'iso_8859_7_1987', 'iso_ir_126'),
    ('iso8859_8', 'csisolatinhebrew', 'hebrew', 'iso_8859_8_1988', 'iso_ir_138'),
    ('iso8859_9', 'csisolatin5', 'iso_8859_9_1989', 'iso_ir_148', 'l5', 'latin5'),
    ('johab', 'cp1361', 'ms1361'),
    ('koi8_r', 'cskoi8r'),
    'koi8_u',
    ('latin_1', '8859', 'cp819', 'csisolatin1', 'ibm819', 'iso8859', 'iso8859_1', 'iso_8859_1', 'iso_8859_1_1987', 'iso_ir_100', 'l1', 'latin'),
    'mac_arabic',
    'mac_centeuro',
    'mac_croatian',
    'mac_cyrillic',
    'mac_farsi',
    'mac_greek',
    'mac_iceland',
    ('mac_latin2', 'maccentraleurope'),
    'mac_roman',
    'mac_romanian',
    'mac_turkish',
    ('mbcs', 'dbcs'),
    'palmos',
    ('ptcp154', 'cp154', 'csptcp154', 'cyrillic_asian', 'pt154'),
    'punycode',
    ('quopri_codec', 'quopri', 'quoted_printable', 'quotedprintable'),
    'raw_unicode_escape',
    'rot_13',
    ('shift_jis', 'csshiftjis', 's_jis', 'sjis'),
    ('shift_jis_2004', 's_jis_2004', 'sjis_2004'),
    ('shift_jisx0213', 's_jisx0213', 'sjisx0213'),
    'string_escape',
    ('tactis', 'tis260'),
    ('tis_620', 'iso_ir_166', 'tis_620_0', 'tis_620_2529_0', 'tis_620_2529_1'),
    'unicode_escape',
    'unicode_internal',
    ('utf_16', 'u16'),
    ('utf_16_be', 'unicodebigunmarked'),
    ('utf_16_le', 'unicodelittleunmarked'),
    ('utf_32', 'u32'),
    'utf_32_be',
    'utf_32_le',
    ('utf_7', 'u7', 'unicode_1_1_utf_7'),
    ('utf_8', 'u8', 'utf', 'utf8_ucs2', 'utf8_ucs4'),
    'utf_8_sig',
    ('uu_codec', 'uu'),
    ('zlib_codec', 'zip', 'zlib'),
    ]

class Codec_ascii(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'ascii'

class Codec_base64_codec(recode.BuiltinStep):
    internal_coding = '<Data>'
    external_coding = 'base64_codec'
    always_strict = True

class Codec_cp037(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp037'

class Codec_cp1006(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1006'

class Codec_cp1026(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1026'

class Codec_cp1140(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1140'

class Codec_cp1250(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1250'

class Codec_cp1251(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1251'

class Codec_cp1252(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1252'

class Codec_cp1253(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1253'

class Codec_cp1254(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1254'

class Codec_cp1255(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1255'

class Codec_cp1256(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1256'

class Codec_cp1257(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1257'

class Codec_cp1258(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp1258'

class Codec_cp424(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp424'

class Codec_cp437(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp437'

class Codec_cp500(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp500'

class Codec_cp720(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp720'

class Codec_cp737(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp737'

class Codec_cp775(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp775'

class Codec_cp850(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp850'

class Codec_cp852(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp852'

class Codec_cp855(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp855'

class Codec_cp856(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp856'

class Codec_cp857(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp857'

class Codec_cp858(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp858'

class Codec_cp860(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp860'

class Codec_cp861(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp861'

class Codec_cp862(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp862'

class Codec_cp863(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp863'

class Codec_cp864(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp864'

class Codec_cp865(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp865'

class Codec_cp866(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp866'

class Codec_cp869(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp869'

class Codec_cp874(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp874'

class Codec_cp875(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp875'

class Codec_cp932(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp932'

class Codec_cp949(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp949'

class Codec_cp950(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'cp950'

class Codec_euc_kr(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'euc_kr'

class Codec_hex_codec(recode.BuiltinStep):
    internal_coding = '<Data>'
    external_coding = 'hex_codec'
    always_strict = True

class Codec_iso8859_10(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_10'

class Codec_iso8859_11(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_11'

class Codec_iso8859_13(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_13'

class Codec_iso8859_14(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_14'

class Codec_iso8859_15(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_15'

class Codec_iso8859_16(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_16'

class Codec_iso8859_2(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_2'

class Codec_iso8859_3(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_3'

class Codec_iso8859_4(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_4'

class Codec_iso8859_5(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_5'

class Codec_iso8859_6(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_6'

class Codec_iso8859_7(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_7'

class Codec_iso8859_8(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_8'

class Codec_iso8859_9(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'iso8859_9'

class Codec_koi8_r(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'koi8_r'

class Codec_latin_1(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'latin_1'

class Codec_mac_arabic(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_arabic'

class Codec_mac_centeuro(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_centeuro'

class Codec_mac_croatian(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_croatian'

class Codec_mac_cyrillic(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_cyrillic'

class Codec_mac_farsi(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_farsi'

class Codec_mac_greek(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_greek'

class Codec_mac_iceland(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_iceland'

class Codec_mac_latin2(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_latin2'

class Codec_mac_roman(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_roman'

class Codec_mac_romanian(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_romanian'

class Codec_mac_turkish(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'mac_turkish'

class Codec_quopri_codec(recode.BuiltinStep):
    internal_coding = '<Data>'
    external_coding = 'quopri_codec'
    always_strict = True

class Codec_raw_unicode_escape(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'raw_unicode_escape'

class Codec_rot_13(recode.BuiltinStep):
    internal_coding = '<Data>'
    external_coding = 'rot_13'
    always_strict = True

class Codec_unicode_escape(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'unicode_escape'

class Codec_unicode_internal(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'unicode_internal'

class Codec_utf_16(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'utf_16'

class Codec_utf_16_be(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'utf_16_be'

class Codec_utf_16_le(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'utf_16_le'

class Codec_utf_32(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'utf_32'

class Codec_utf_32_be(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'utf_32_be'

class Codec_utf_32_le(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'utf_32_le'

class Codec_utf_7(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'utf_7'

class Codec_utf_8(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'utf_8'

class Codec_utf_8_sig(recode.BuiltinStep):
    internal_coding = '<Ustring>'
    external_coding = 'utf_8_sig'

class Codec_uu_codec(recode.BuiltinStep):
    internal_coding = '<Data>'
    external_coding = 'uu_codec'
    always_strict = True

class Codec_zlib_codec(recode.BuiltinStep):
    internal_coding = '<Data>'
    external_coding = 'zlib_codec'
    always_strict = True
