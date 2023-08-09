cmake_minimum_required(VERSION 3.15)
project(demo)

set(SOCKET_SERVER socket_server)
set(SOCKET_CLIENT socket_client)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/bin) # 二进制文件
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib) # 动态库
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib) # 静态库

option(USE_SUPER_PRINT "use the super printf" ON)

configure_file(version.h.in version.h)

include_directories("${PROJECT_BINARY_DIR}" include)

# add_executable(${SOCKET_SERVER} src/socket_server.cpp)
# add_executable(${SOCKET_CLIENT} src/socket_client.cpp)
add_executable(${PROJECT_NAME} src/demo.cpp)

add_library(compiler_flags INTERFACE)
target_compile_features(compiler_flags INTERFACE cxx_std_11)

if(USE_SUPER_PRINT)
  add_subdirectory(src/super_printf)
  message("use super print")
  list(APPEND EXTRA_LIB super_print)
  # list(APPEND EXTRA_LIB_INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/lib)
endif()
# target_include_directories(${PROJECT_NAME} PUBLIC
# ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_link_directories(${PROJECT_NAME} PUBLIC ${EXTRA_LIB_INCLUDE})
message("fef" ${EXTRA_LIB_INCLUDE})
# message("fef" ${EXTRA_LIB})
target_link_libraries(${PROJECT_NAME} PUBLIC ${EXTRA_LIB} compiler_flags)

install(TARGETS ${PROJECT_NAME} DESTINATION bin)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/src/super_print.h DESTINATION include)
install(EXPORT SuperPrintExportTargets FILE SuperPrintExportTargets.cmake DESTINATION lib/cmake/super_print)

include(CTest)
# enable_testing()
add_test(NAME T1 COMMAND demo)
set_tests_properties(T1 PROPERTIES PASS_REGULAR_EXPRESSION "version: 1.0*")
