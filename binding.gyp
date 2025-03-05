{
  "targets": [
    {
      "target_name": "assaddon",
      "sources": [ "addon.cpp", "src/ass_measure.c" ],
      "include_dirs": [
  "<!@(node -p \"require('node-addon-api').include\")",
  "include",
  "<!@(pkg-config --cflags-only-I libass | sed 's/-I//g')"
],
      "libraries": [
        "<!@(pkg-config --libs libass)"
      ],
      "defines": [ "NAPI_CPP_EXCEPTIONS" ],
      "cflags": ["-fPIC", "-O2"],
      "cflags_cc": ["-fPIC", "-O2"],
      "xcode_settings": {
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "CLANG_CXX_LIBRARY": "libc++",
        "MACOSX_DEPLOYMENT_TARGET": "10.15"
      },
      "msvs_settings": {
        "VCCLCompilerTool": { "ExceptionHandling": 1 }
      }
    }
  ]
}

