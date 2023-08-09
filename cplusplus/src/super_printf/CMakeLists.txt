add_library(super_print super_printf.cpp inc/test.cpp)
message("super" ${CMAKE_CURRENT_SOURCE_DIR})
target_include_directories(super_print INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(super_print compiler_flags)

set(installable_libs super_print compiler_flags)
install(TARGETS ${installable_libs} EXPORT SuperPrintExportTargets DESTINATION lib)
install(FILES inc/test.h DESTINATION include)
