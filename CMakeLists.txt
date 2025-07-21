cmake_minimum_required(VERSION 3.8)
project(rviz_panel_gui)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rosbag2_interfaces REQUIRED)
find_package(pluginlib REQUIRED)
find_package(rviz_common REQUIRED)
find_package(rviz_rendering REQUIRED)
find_package(rviz_default_plugins REQUIRED)
find_package(rosbag2_cpp REQUIRED)
find_package(rosbag2_transport REQUIRED)
find_package(rosbag2_storage REQUIRED)
find_package(Qt5 REQUIRED COMPONENTS Widgets)

include_directories(
  include
  ${rosbag2_cpp_INCLUDE_DIRS}
  ${rosbag2_transport_INCLUDE_DIRS}
)
## Qt5 boilerplate options from http://doc.qt.io/qt-5/cmake-manual.html
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
## Prefer the Qt signals and slots to avoid defining "emit", "slots",
## etc because they can conflict with boost signals, so define QT_NO_KEYWORDS here.
set(CMAKE_AUTOMOC_COMPILER_PREDEFINES OFF)
add_definitions(-DQT_NO_KEYWORDS)

pluginlib_export_plugin_description_file(rviz_common plugin_description.xml)

install(
  TARGETS
  EXPORT
    export_${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
  INCLUDES DESTINATION include
)

if(CMAKE_SYSTEM_PROCESSOR MATCHES "^(x86_64|AMD64)$")
  message("Detected architecture: x86")
  install(FILES x86/libfile_selector.so DESTINATION lib)
  install(FILES x86/libros_bag_gui.so DESTINATION lib)
elseif(CMAKE_SYSTEM_PROCESSOR MATCHES "^(aarch64|arm64)$")
  message("Detected architecture: arm64")
  install(FILES arm64/libfile_selector.so DESTINATION lib)
  install(FILES arm64/libros_bag_gui.so DESTINATION lib)
else()
  message(WARNING "Unknown architecture: ${CMAKE_SYSTEM_PROCESSOR}")
endif()

install(DIRECTORY launch 
  DESTINATION share/${PROJECT_NAME})

ament_package()
