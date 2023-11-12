cmake_minimum_required(VERSION 3.15)
project(demo)

set(SOCKET_SERVER socket_server)
set(SOCKET_CLIENT socket_client)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/bin) # 二进制文件
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib) # 动态库
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/lib) # 静态库

add_executable(${PROJECT_NAME} src/main.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC include)

find_package(spdlog CONFIG REQUIRED)
target_link_libraries(${PROJECT_NAME} PRIVATE spdlog::spdlog)

# Or use the header-only version
find_package(spdlog CONFIG REQUIRED)
target_link_libraries(${PROJECT_NAME} PRIVATE spdlog::spdlog_header_only)

find_package(nlohmann_json CONFIG REQUIRED)
target_link_libraries(${PROJECT_NAME} PRIVATE nlohmann_json::nlohmann_json)

find_package(mosquitto REQUIRED)
target_include_directories(${PROJECT_NAME}  PRIVATE ${MOSQUITTO_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME}  PRIVATE ${MOSQUITTO_LIBRARIES})

# target_link_directories(${PROJECT_NAME} PUBLIC ${EXTRA_LIB_INCLUDE})
# target_link_libraries(${PROJECT_NAME} PUBLIC ${EXTRA_LIB} compiler_flags)

# install(TARGETS ${PROJECT_NAME} DESTINATION bin)
# install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/src/super_print.h DESTINATION include)
