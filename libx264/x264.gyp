{
  'variables': {
    'conditions': [
      ['OS == "linux"', {
        'use_system_x264%': 0,
      }, {
        'use_system_x264%': 0,
      }],
    ],
    'conditions': [
      ['target_arch == "armv7" and target_arch == "arm_neon"', {
        # Need a separate config for arm+neon vs arm
        'x264_config%': 'arm-neon',
      }, {
        'x264_config%': '<(target_arch)',
      }],
      ['OS == "mac" or OS == "win" or OS == "openbsd"', {
        'os_config%': '<(OS)',
      }, {  # all other Unix OS's use the linux config
        'os_config%': 'linux',
      }],
    ],

    'use_system_x264%': 0,

    # Locations for generated artifacts.
    'shared_generated_dir': '<(SHARED_INTERMEDIATE_DIR)/third_party/x264',
  },

  'conditions': [
    ['use_system_x264 == 1', {
      'targets': [
        {
          'target_name': 'x264',
          'type': 'none',
          'link_settings': {
            'libraries': [
              '-lx264',
            ],
          },
        }, # target
      ],
    }, { # else: use_system_x264 != 1
      'targets': [
        {
          'target_name': 'x264',
            # TODO(kyan): Provide shared_library support.
          'type': 'static_library',

          'direct_dependent_settings': {
            'include_dirs': [
              '<(platform_config_root)',
              '<(x264_source_dir)',
              '.',
            ],
          }, # direct_dependent_settings

          'includes': [
            'x264_generated.gypi',
          ], # includes

          'variables': {
            'platform_config_root': 'config/<(os_config)/<(x264_config)',
          }, # variables

          
          'cflags': [
            '-Wshadow',
            '-Wno-unused-function',
            '-ffast-math',
            '-fomit-frame-pointer',
            '-fno-tree-vectorize',
          ], # cflags

          'msvs_settings': {
            'VCCLCompilerTool': {
              'CompileAs': '1',
              #'DisableSpecificWarnings': '4996',
            },
            'VCLibrarianTool': {
            }
          }, # msvs_settings

	      'msvs_disabled_warnings': [
            4003, 4018, 4305,
          ],
	
          'include_dirs': [
            '<(platform_config_root)',
            '<(x264_source_dir)',
          ],

          'dependencies': [
            'x264_yasm',
          ],

          'sources': [
            '<(platform_config_root)/config.h',
            '<(platform_config_root)/x264_config.h',
            '<@(c_sources)',
          ], # sources

          'conditions': [
            [ 'OS == "win"', {
              'defines': [
                '_LIB',
              ],
            }],
            ['OS == "linux"', {
              'cflags': ['-std=gnu99'],
            }, {
              'cflags': ['-std=c99'],
            }],
          ], # conditions
        }, # target x264
        {
          'target_name': 'x264_yasm',
          'type': 'static_library',
          # VS2010 does not correctly incrementally link obj files generated
          # from asm files. This flag disables UseLibraryDependencyInputs to
          # avoid this problem.
          'msvs_2010_disable_uldi_when_referenced': 1,
          'includes': [
            'x264_generated.gypi',
            '../../yasm/yasm_compile.gypi',
          ],
          'sources': [
            '<@(asm_sources)',
            # XCode doesn't want to link a pure assembly target and will fail
            # to link when it creates an empty file list.  So add a dummy file
            # keep the linker happy.  See http://crbug.com/157073
            #'xcode_hack.c',
          ],
          'variables': {
            # Path to platform configuration files.
            'platform_config_root': 'config/<(os_config)/<(x264_config)',
            'conditions': [
              ['target_arch == "ia32"', {
                'more_yasm_flags': [
                  '-DARCH_X86_64=0',
                ],
              }, {
                'more_yasm_flags': [
                  '-DARCH_X86_64=1',
                ],
              }],
              ['OS == "mac"', {
                'more_yasm_flags': [
                  # Necessary to ensure symbols end up with a _ prefix; added by
                  # yasm_compile.gypi for Windows, but not Mac.
                  '-DPREFIX',
                ]
              }],
            ],
            'yasm_flags': [
              '-DPIC',
              '-DHIGH_BIT_DEPTH=0',
              '-DBIT_DEPTH=8',
              '-DHAVE_ALIGNED_STACK=1',
              '>@(more_yasm_flags)',
              '-I', '<(platform_config_root)',
              '-I', '<(x264_source_dir)/common/x86/',
              # Disable warnings, prevents log spam for things we won't fix.
              '-w',
            ],
            'yasm_output_path': '<(shared_generated_dir)/yasm'
          },
        }, # target x264_yasm
      ]
    }], # conditions
  ],
}
