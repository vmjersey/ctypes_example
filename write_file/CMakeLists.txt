add_library(write_file SHARED
    write_file.c
  )

target_include_directories(write_file PRIVATE .)

install(TARGETS write_file
    DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
    )
