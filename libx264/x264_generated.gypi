# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# NOTE: this file is autogenerated by ffmpeg/scripts/generate_gyp.py

{
  'variables': {
    'x264_source_dir': 'x264_src',
    'conditions': [
      ['(target_arch == "ia32" or target_arch == "x64") and (1) and (1)', {
        'asm_sources': [
          'x264_src/common/x86/bitstream-a.asm',
          'x264_src/common/x86/cabac-a.asm',
          'x264_src/common/x86/const-a.asm',
          'x264_src/common/x86/cpu-a.asm',
          'x264_src/common/x86/dct-a.asm',
          'x264_src/common/x86/deblock-a.asm',
          'x264_src/common/x86/mc-a.asm',
          'x264_src/common/x86/mc-a2.asm',
          'x264_src/common/x86/pixel-a.asm',
          'x264_src/common/x86/predict-a.asm',
          'x264_src/common/x86/quant-a.asm',
          'x264_src/common/x86/sad-a.asm',
        ],
      }],  # (target_arch == "ia32" or target_arch == "x64") and (1) and (1)
      ['target_arch == "x64"', {
        'asm_sources': [
          'x264_src/common/x86/dct-64.asm',
          'x264_src/common/x86/trellis-64.asm',
        ],
      }], #target_arch == "x64"
      ['target_arch == "ia32"', {
        'asm_sources': [
          'x264_src/common/x86/dct-32.asm',
          'x264_src/common/x86/pixel-32.asm',
        ],
      }], #target_arch == "ia32"
      ['target_arch == "arm"',{
        'c_sources':[
          'x264_src/common/arm/mc-c.c',
          'x264_src/common/arm/predict-c.c',
          'x264_src/common/arm/cpu-a.S',
          'x264_src/common/arm/pixel-a.S',
          'x264_src/common/arm/mc-a.S',
          'x264_src/common/arm/dct-a.S',
          'x264_src/common/arm/quant-a.S',
          'x264_src/common/arm/deblock-a.S',
          'x264_src/common/arm/predict-a.S',
          'x264_src/common/arm/bitstream-a.S',
        ],
        'asm_sources': [
        ],
      }], #target_arch == "arm"
      ['OS == "win"', {
        'c_sources': [
          'x264_src/common/win32thread.c',
        ],
      }], #OS == "win"
    ],  # conditions
    'c_sources': [
      'x264_src/common/bitstream.c',
      'x264_src/common/cabac.c',
      'x264_src/common/common.c',
      'x264_src/common/cpu.c',
      'x264_src/common/dct.c',
      'x264_src/common/deblock.c',
      'x264_src/common/frame.c',
      'x264_src/common/macroblock.c',
      'x264_src/common/mc.c',
      'x264_src/common/mvpred.c',
      'x264_src/common/osdep.c',
      'x264_src/common/pixel.c',
      'x264_src/common/predict.c',
      'x264_src/common/quant.c',
      'x264_src/common/rectangle.c',
      'x264_src/common/set.c',
      'x264_src/common/threadpool.c',
      'x264_src/common/vlc.c',
      'x264_src/common/x86/mc-c.c',
      'x264_src/common/x86/predict-c.c',
      'x264_src/encoder/analyse.c',
      'x264_src/encoder/cabac.c',
      'x264_src/encoder/cavlc.c',
      'x264_src/encoder/encoder.c',
      'x264_src/encoder/lookahead.c',
      'x264_src/encoder/macroblock.c',
      'x264_src/encoder/me.c',
      'x264_src/encoder/ratecontrol.c',
      'x264_src/encoder/set.c',
    ],  # c_sources
    'c_headers': [
      'x264_src/x264cli.h',
      'x264_src/x264.h',
      'x264_src/extras/stdint.h',
      'x264_src/extras/getopt.h',
      'x264_src/extras/inttypes.h',
      'x264_src/extras/avisynth_c.h',
      'x264_src/common/quant.h',
      'x264_src/common/predict.h',
      'x264_src/common/display.h',
      'x264_src/common/set.h',
      'x264_src/common/threadpool.h',
      'x264_src/common/mc.h',
      'x264_src/common/dct.h',
      'x264_src/common/macroblock.h',
      'x264_src/common/common.h',
      'x264_src/common/rectangle.h',
      'x264_src/common/pixel.h',
      'x264_src/common/cpu.h',
      'x264_src/common/cabac.h',
      'x264_src/common/bitstream.h',
      'x264_src/common/visualize.h',
      'x264_src/common/frame.h',
      'x264_src/common/osdep.h',
      'x264_src/common/win32thread.h',
      'x264_src/common/x86/quant.h',
      'x264_src/common/x86/predict.h',
      'x264_src/common/x86/mc.h',
      'x264_src/common/x86/dct.h',
      'x264_src/common/x86/pixel.h',
      'x264_src/common/x86/util.h',
      'x264_src/common/ppc/quant.h',
      'x264_src/common/ppc/predict.h',
      'x264_src/common/ppc/mc.h',
      'x264_src/common/ppc/dct.h',
      'x264_src/common/ppc/pixel.h',
      'x264_src/common/ppc/ppccommon.h',
      'x264_src/common/arm/quant.h',
      'x264_src/common/arm/predict.h',
      'x264_src/common/arm/mc.h',
      'x264_src/common/arm/dct.h',
      'x264_src/common/arm/pixel.h',
      'x264_src/common/sparc/pixel.h',
      'x264_src/filters/filters.h',
      'x264_src/filters/video/video.h',
      'x264_src/filters/video/internal.h',
      'x264_src/input/input.h',
      'x264_src/encoder/analyse.h',
      'x264_src/encoder/set.h',
      'x264_src/encoder/macroblock.h',
      'x264_src/encoder/ratecontrol.h',
      'x264_src/encoder/me.h',
      'x264_src/output/output.h',
      'x264_src/output/flv_bytestream.h',
      'x264_src/output/matroska_ebml.h',
    ],  # c_headers
  },
}
