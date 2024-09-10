# Content from pr-agent.1124034.md

# Text from pr-agent.1124034.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/3

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/onboard_msg/scripts/launch_CLI_test.sh?ref_type=heads#L14-L15'><strong>可能的错误</strong></a><br>在行14和行15中，`RECORD_PATH`和`RECORD_NAME`变量在使用时没有加双引号，可能会导致路径解析错误。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/onboard_msg/scripts/launch_CLI_test.sh?ref_type=heads#L24-L25'><strong>代码异味</strong></a><br>在行24和行25中，`RECORD_PATH`和`RECORD_NAME`变量在使用时没有加双引号，可能会导致路径解析错误。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/onboard_msg/scripts/build_to_tmp.sh?ref_type=heads#L7-L7'><strong>代码异味</strong></a><br>在行7中，使用`sudo`进行文件复制操作，可能会引入权限问题。建议检查是否有必要使用`sudo`。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/onboard_msg/mipilot/proto/perception/obstacle_detection.proto?ref_type=heads#L53-L53'><strong>可能的错误</strong></a><br>在行53中，添加了新的枚举值`LATERAL_BEHAVIOR_NUDGE`，但没有相应的文档或注释说明其用途。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/onboard_msg/mipilot/proto/perception/obstacle_detection.proto?ref_type=heads#L273-L274'><strong>可能的错误</strong></a><br>在行273和行274中，`VEHICLE_DOOR_STATUS_RIGHT_OPEN`和`VEHICLE_DOOR_STATUS_LEFT_OPEN`的顺序与旧代码中的顺序不一致，可能会导致潜在的兼容性问题。

</td></tr>
</table>



---

# Content from pr-agent.1131659.md

# Text from pr-agent.1131659.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/19

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 4 🔵🔵🔵🔵⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/l3_localization/mipilot/modules/L3/localization/geoloc/apps/data_filter.cc?ref_type=heads#L39-L43'><strong>代码异味</strong></a><br>代码中有大量注释掉的代码块（例如行39-43和行69-73），这些代码块应该被移除以保持代码的整洁和可读性。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/l3_localization/mipilot/modules/L3/localization/geoloc/apps/data_filter.cc?ref_type=heads#L69-L73'><strong>代码异味</strong></a><br>代码中有大量注释掉的代码块（例如行69-73），这些代码块应该被移除以保持代码的整洁和可读性。

</td></tr>
</table>



---

# Content from pr-agent.1127793.md

# Text from pr-agent.1127793.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/9

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/fix/oracle_core/mipilot/modules/perception_fusion/common/oracle/traj/traj_manager.cpp?ref_type=heads#L36-L72'><strong>性能问题</strong></a><br>在行36-72中，添加了一个新的逻辑块来删除过多的NPC轨迹。这个逻辑块包含了多个嵌套循环和复杂的计算，可能会影响性能。建议对这部分代码进行性能测试，确保其不会显著影响系统的整体性能。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/fix/oracle_core/mipilot/modules/perception_fusion/modules/oracle/offline_cpp/oracle_module_offline.cc?ref_type=heads#L45-L45'><strong>代码异味</strong></a><br>在行45中，`RECORD_PATH`的定义使用了硬编码的路径。这种做法不利于代码的可维护性和可配置性。建议将路径配置为可配置的参数，而不是硬编码在代码中。

</td></tr>
</table>



---

# Content from pr-agent.1128491.md

# Text from pr-agent.1128491.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/11

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/oracle_multi_mv2d/mipilot/modules/perception_fusion/common/oracle/traj/traj.cpp?ref_type=heads#L297-L297'><strong>可能的错误</strong></a><br>在行297，`proj_info.contour_dl_var`的赋值从`proj_info.contour_enu_var`变为`proj_info.contour_imu_var`。请确认这个变化是否正确，并验证其他相关变量的赋值是否一致。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/oracle_multi_mv2d/mipilot/modules/perception_fusion/common/oracle/traj/traj.cpp?ref_type=heads#L317-L328'><strong>代码异味</strong></a><br>在行317-328，多个变量的赋值从`enu_var`变为`imu_var`。请确认这些变化是否一致，并验证是否需要对其他相关代码进行类似的修改。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/oracle_multi_mv2d/mipilot/modules/perception_fusion/common/oracle/frame/input_frame.h?ref_type=heads#L20-L21'><strong>代码异味</strong></a><br>在行20-21，`FormatMV2DInfo`函数的参数类型从`Obstacle3d`变为`AssociatedObstacle3d`。请确认这个变化是否正确，并验证其他相关函数的参数类型是否一致。

</td></tr>
</table>



---

# Content from pr-agent.1134430.md

# Text from pr-agent.1134430.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/26

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 2 🔵🔵⚪⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/dev/pred/mipilot/modules/perception/common/prediction/executor_units/multipathpp/multipathpp_output_unit.cc?ref_type=heads#L258-L258'><strong>可能的错误</strong></a><br>在行258，`position.z()`的值可能未定义或未初始化，可能导致错误。请确保`position.z()`在使用前已正确初始化。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/dev/pred/mipilot/modules/perception/common/prediction/executor_units/multipathpp/multipathpp_output_unit.cc?ref_type=heads#L312-L312'><strong>代码异味</strong></a><br>在行312，将`z`值硬编码为0.0可能不是最佳实践。请考虑是否有更合适的方法来设置`z`值。

</td></tr>
</table>



---

# Content from pr-agent.1130583.md

# Text from pr-agent.1130583.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/13

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/update_calib/mipilot/modules/perception/common/lidar/preprocess/reset_lidar_world_unit.cc?ref_type=heads#L138-L145'><strong>代码注释</strong></a><br>行138-145的代码被注释掉了，请确认这些代码是否仍然需要。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/update_calib/mipilot/modules/perception/modules/lidar/perception_lidar_module.cc?ref_type=heads#L475-L475'><strong>TODO注释</strong></a><br>行475的TODO注释需要进一步处理或移除。

</td></tr>
</table>



---

# Content from pr-agent.1135894.md

# Text from pr-agent.1135894.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/33

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/fix/oracle_offline_flag/mipilot/modules/perception_fusion/modules/oracle/offline_visualizer/log_reader.py?ref_type=heads#L17-L19'><strong>可能的错误</strong></a><br>行17-19中的try-except块可能会掩盖其他潜在的异常，建议在except块中添加更具体的异常处理。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/fix/oracle_offline_flag/mipilot/modules/perception_fusion/modules/oracle/offline_visualizer/log_reader.py?ref_type=heads#L23-L25'><strong>代码异味</strong></a><br>行23-25中的注释代码可能会导致混淆，建议删除不必要的注释代码。

</td></tr>
</table>



---

# Content from pr-agent.1134047.md

# Text from pr-agent.1134047.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/25

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/resolve_oracle_warn/mipilot/modules/perception_fusion/common/oracle/frame/vel_estimator.cpp?ref_type=heads#L173-L174'><strong>代码异味</strong></a><br>行173-174和行186-187的注释代码可能需要移除或重新启用。请确认这些调试信息是否仍然需要。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/resolve_oracle_warn/mipilot/modules/perception_fusion/common/oracle/frame/input_frame.cpp?ref_type=heads#L10-L10'><strong>代码异味</strong></a><br>行10的`[[maybe_unused]]`属性可能不需要。请确认是否需要保留。

</td></tr>
</table>



---

# Content from pr-agent.1134588.md

# Text from pr-agent.1134588.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/27

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mimir_gpu_device/scripts/build_to_docker.sh?ref_type=heads#L1-L22'><strong>代码异味</strong></a><br>在行1-22中，脚本的逻辑和结构发生了较大变化，建议检查新增逻辑是否正确，特别是条件判断和文件路径的处理。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mimir_gpu_device/scripts/build_to_tmp.sh?ref_type=heads#L1-L19'><strong>代码异味</strong></a><br>在行1-19中，脚本的逻辑和结构发生了较大变化，建议检查新增逻辑是否正确，特别是条件判断和文件路径的处理。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mimir_gpu_device/build/scripts/build_l3modules_offline.sh?ref_type=heads#L1-L19'><strong>代码异味</strong></a><br>在行1-19中，新增了一个完整的构建脚本，建议检查构建配置和参数是否正确。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mimir_gpu_device/mipilot/modules/L3/pnc/mimir/trajectory_generator/cuda_trajectory_generator.h?ref_type=heads#L72-L78'><strong>可能的错误</strong></a><br>在行72-78中，`device_id`的初始化和条件编译逻辑发生了变化，建议检查是否存在潜在的逻辑错误。

</td></tr>
</table>



---

# Content from pr-agent.1133939.md

# Text from pr-agent.1133939.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/24

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mimir_bugfix/mipilot/modules/L3/pnc/mimir/common/trajectory/trajectory.cpp?ref_type=heads#L32-L33'><strong>可能的错误</strong></a><br>在行33，`std::ceil`函数的参数中减去了`1e-6`，这可能会导致计算结果不准确。请确认这个修改的合理性。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mimir_bugfix/mipilot/modules/L3/pnc/mimir/common/trajectory/trajectory.cpp?ref_type=heads#L69-L69'><strong>可能的错误</strong></a><br>在行69，`std::distance`函数的参数顺序改变了，可能会导致计算结果不正确。请确认这个修改的合理性。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mimir_bugfix/mipilot/modules/L3/pnc/mimir/common/trajectory/trajectory.cpp?ref_type=heads#L136-L136'><strong>可能的错误</strong></a><br>在行136，`for`循环的条件从`i < num`改为`i + 1 < num`，这可能会导致循环次数减少。请确认这个修改的合理性。

</td></tr>
</table>



---

# Content from pr-agent.1128625.md

# Text from pr-agent.1128625.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/12

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 4 🔵🔵🔵🔵⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mainandrobin/mipilot/modules/perception/common/mv2d_fusion/create_mv_global_bbox_obstacle_unit.cc?ref_type=heads#L59-L75'><strong>代码异味</strong></a><br>代码中有多个TODO注释，需要进一步处理和完善。例如，行59和行75的TODO注释。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mainandrobin/mipilot/modules/perception/common/mv2d_fusion/create_mv_global_bbox_obstacle_unit.cc?ref_type=heads#L75-L75'><strong>可能的错误</strong></a><br>行75的TODO注释提到了相对速度的计算，需要确认这个计算是否正确。

</td></tr>
</table>



---

# Content from pr-agent.1135124.md

# Text from pr-agent.1135124.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/30

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 4 🔵🔵🔵🔵⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mimir_bugfix/mipilot/modules/L3/pnc/plmap/src/plmap/plsequence.cpp?ref_type=heads#L39-L91'><strong>代码重复</strong></a><br>在行39-63和行67-91之间有大量重复代码。考虑将重复的逻辑提取到一个单独的函数中以提高代码可读性和可维护性。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/mimir_bugfix/mipilot/modules/L3/pnc/plmap/src/plmap/plsequence.cpp?ref_type=heads#L101-L135'><strong>日志信息</strong></a><br>在行101和行135添加了日志信息。请确保这些日志信息是必要的，并且不会影响性能。

</td></tr>
</table>



---

# Content from pr-agent.1124421.md

# Text from pr-agent.1124421.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/6

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 4 🔵🔵🔵🔵⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/mv2d_seq_asso/mipilot/modules/perception_fusion/common/oracle/traj/traj_manager.cpp?ref_type=heads#L36-L72'><strong>性能问题</strong></a><br>在行36-72中，添加了一个复杂的逻辑用于删除过多的NPC。这段代码可能会影响性能，特别是在`_tracker_frame.all_tids.size()`较大时。需要评估这段代码的性能影响，并考虑是否有更高效的实现方式。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/mv2d_seq_asso/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L113-L113'><strong>代码异味</strong></a><br>在行113中，移除了对`is_pilot_car_mode`的检查，直接调用了`ConvertObjectDetectionTypeToInternalObjectType`。需要确认这种简化是否会影响功能，并考虑是否需要保留原有的条件判断。

</td></tr>
</table>



---

# Content from pr-agent.1134916.md

# Text from pr-agent.1134916.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/29

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/fix/oracle_heading/mipilot/modules/perception_fusion/common/oracle/traj/traj.cpp?ref_type=heads#L267-L267'><strong>可能的错误</strong></a><br>在行267，`sel_heading`被设置为0.0F，这可能会导致后续计算中的问题。请确认这是否是预期行为。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/fix/oracle_heading/mipilot/modules/perception_fusion/common/oracle/traj/traj.cpp?ref_type=heads#L335-L337'><strong>代码异味</strong></a><br>在行335-337，有注释掉的代码块。请确认这些代码是否仍然需要，或者是否可以删除。

</td></tr>
</table>



---

# Content from pr-agent.1124772.md

# Text from pr-agent.1124772.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/8

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 4 🔵🔵🔵🔵⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/addrobin/mipilot/ados/python/sensor_converter/lidar/innovusion/robin_w_convert.cc?ref_type=heads#L37-L60'><strong>代码异味</strong></a><br>在行37-60，函数`ConvertRobinWLidarMessageToPointCloud`中，变量`internal_calibration`的类型是`std::vector<int8_t>`，但`paras`的类型是`std::string`。直接将`paras`的字符转换为`int8_t`可能会导致数据解释错误。建议明确`paras`的数据格式和转换逻辑。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/addrobin/mipilot/ados/sensors/lidar/lidar_factory.cc?ref_type=heads#L58-L63'><strong>代码异味</strong></a><br>在行58-63，添加了新的`case`语句，但没有对`RobinW`类进行详细的单元测试或集成测试。建议添加相关测试以确保新功能的正确性和稳定性。

</td></tr>
</table>



---

# Content from pr-agent.1133454.md

# Text from pr-agent.1133454.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/23

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/l3_image_channel/mipilot/modules/perception/pilot/apps/mv2d_fusion/mv2d_fusion_app.cc?ref_type=heads#L128-L136'><strong>代码异味</strong></a><br>在行128-136，添加了大量的调试信息输出。这些信息输出可能会影响性能，建议在生产环境中移除或使用日志级别控制。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/l3_image_channel/scripts/launch_CLI_test.sh?ref_type=heads#L25-L25'><strong>可能的错误</strong></a><br>在行25，添加了`-u`参数，但没有解释其用途。请确保这个参数是必要的，并在代码中添加相应的注释。

</td></tr>
</table>



---

# Content from pr-agent.1124675.md

# Text from pr-agent.1124675.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/7

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 2 🔵🔵⚪⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/bugfix/fix_lidardet_typeerror/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L113-L113'><strong>可能的错误</strong></a><br>在行113，`ConvertObjectDetectionTypeToInternalObjectType`函数的调用可能需要检查`det_raw.at(8)`的值是否在预期范围内，以避免潜在的类型错误。

</td></tr>
</table>



---

# Content from pr-agent.1133302.md

# Text from pr-agent.1133302.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/22

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 2 🔵🔵⚪⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/stackev3/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.h?ref_type=heads#L79-L81'><strong>代码异味</strong></a><br>在头文件中创建大张量可能会导致内存管理问题。建议将张量的创建移到实现文件中。

</td></tr>
</table>



---

# Content from pr-agent.1131528.md

# Text from pr-agent.1131528.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/18

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/resolve_deps/scripts/repo_dependency/find_missing_repo.py?ref_type=heads#L29-L29'><strong>可能的错误</strong></a><br>在行29，`all_access_repos` 被重新赋值，导致之前的值丢失。应该使用 `all_access_repos = [repo.replace("onboard/", "//") for repo in all_access_repos]` 来保留之前的值。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/resolve_deps/scripts/repo_dependency/find_missing_repo.py?ref_type=heads#L55-L58'><strong>代码异味</strong></a><br>在行55-58，`has_access` 变量的类型不一致，有时是布尔值，有时是字符串。建议统一类型。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/resolve_deps/scripts/repo_dependency/run.sh?ref_type=heads#L7-L10'><strong>代码异味</strong></a><br>在行7-10，`ssh` 命令的输出文件名应该使用双引号括起来，以避免空格或特殊字符导致的问题。

</td></tr>
</table>



---

# Content from pr-agent.1123693.md

# Text from pr-agent.1123693.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/1

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/settingup/pull_third_party.sh?ref_type=heads#L18-L18'><strong>可能的错误</strong></a><br>在行18，`printf $dir_name` 缺少引号，可能导致意外的行为。建议改为 `printf "$dir_name"`。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/settingup/pull_third_party.sh?ref_type=heads#L29-L29'><strong>代码异味</strong></a><br>在行29，`git clone` 命令中的URL应该使用变量来构建，以提高可读性和可维护性。

</td></tr>
</table>



---

# Content from pr-agent.1127964.md

# Text from pr-agent.1127964.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/10

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 4 🔵🔵🔵🔵⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/mv2d/mipilot/modules/perception/pilot/nets/camera/mv2d_net.cc?ref_type=heads#L17-L23'><strong>代码异味</strong></a><br>在行17-23，包含了许多不必要的头文件。请检查并移除不必要的头文件。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/mv2d/mipilot/modules/perception/pilot/nets/camera/mv2d_net.cc?ref_type=heads#L34-L34'><strong>可能的错误</strong></a><br>在行34，`ADS_INFO`日志输出中缺少换行符，可能导致日志输出不清晰。建议在日志信息末尾添加换行符。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/mv2d/mipilot/modules/perception/pilot/nets/camera/mv2d_net.cc?ref_type=heads#L53-L61'><strong>代码异味</strong></a><br>在行53-61，`cudaMemcpyAsync`调用中使用了硬编码的数据类型`char`。建议使用模板或类型推导来提高代码的可读性和可维护性。

</td></tr>
</table>



---

# Content from pr-agent.1132170.md

# Text from pr-agent.1132170.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/20

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 4 🔵🔵🔵🔵⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/add_pnc/mipilot/modules/L3/pnc/control/controller/core/tracking_algorithm/lqr_controller.cc?ref_type=heads#L32-L33'><strong>代码异味</strong></a><br>在行32-33，矩阵尺寸检查的条件可以简化为一个条件。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/add_pnc/mipilot/modules/L3/pnc/control/controller/core/tracking_algorithm/lqr_controller.cc?ref_type=heads#L48-L57'><strong>可能的错误</strong></a><br>在行48-57，闭环稳定性检查中，应确保所有特征值的实部都小于0。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/add_pnc/mipilot/modules/L3/pnc/control/controller/core/tracking_algorithm/lqr_controller.cc?ref_type=heads#L73-L83'><strong>性能问题</strong></a><br>在行73-83，特征值和特征向量的计算可能会影响性能，建议优化或缓存结果。

</td></tr>
</table>



---

# Content from pr-agent.1124333.md

# Text from pr-agent.1124333.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/5

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

敏感信息暴露：Dockerfile中的`system.json`文件包含敏感信息，如`vin_code`和`vid_code`，可能需要进一步保护。</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/add_docker_file/scripts/launch_CLI_test.sh?ref_type=heads#L18-L23'><strong>代码重复</strong></a><br>新增的节点启动命令与旧代码中的命令重复，可能需要进一步检查是否有必要重复添加。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/add_docker_file/docker_builder/launch_CLI_test.sh?ref_type=heads#L9-L21'><strong>代码重复</strong></a><br>新增的节点启动命令与旧代码中的命令重复，可能需要进一步检查是否有必要重复添加。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/add_docker_file/scripts/build_to_docker.sh?ref_type=heads#L1-L13'><strong>代码可读性</strong></a><br>脚本中的路径和命令可能需要更多的注释以提高可读性。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/add_docker_file/docker_builder/Dockerfile?ref_type=heads#L12-L12'><strong>安全性</strong></a><br>Dockerfile中的`RUN chmod -R 777 /map`命令赋予了所有用户对`/map`目录的完全权限，可能存在安全风险。

</td></tr>
</table>



---

# Content from pr-agent.1134722.md

# Text from pr-agent.1134722.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/28

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/ctrl/mipilot/modules/L3/pnc/control/controller/core/longitudinal_processor.cc?ref_type=heads#L221-L238'><strong>代码异味</strong></a><br>在`RecordLngRefTraj`函数中，`KWhlTrqIdx`变量名应改为`kWhlTrqIdx`以保持一致性。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/ctrl/mipilot/proto/pilot/l3_pnc/control_debug_info.proto?ref_type=heads#L275-L288'><strong>可能的错误</strong></a><br>在`LngRefPoint`消息中，`accel`字段的注释应为“Longitudinal acceleration”，而不是“Longitudinal speed”。

</td></tr>
</table>



---

# Content from pr-agent.1135579.md

# Text from pr-agent.1135579.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/32

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 4 🔵🔵🔵🔵⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/tracklet_asso_move_to_l3/mipilot/modules/L3/perception/apps/tracklet_asso/app/tracklet_asso_mipilot_app.cc?ref_type=heads#L75-L75'><strong>代码异味</strong></a><br>行75中的FIXME注释表明代码中有一个临时的调试模式启用标志，需要进一步处理。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/tracklet_asso_move_to_l3/mipilot/modules/L3/perception/apps/tracklet_asso/app/tracklet_asso_mipilot_app.cc?ref_type=heads#L88-L92'><strong>可能的错误</strong></a><br>行88和行92中的注释代码可能表示未完成的功能或临时解决方案，需要进一步审查。

</td></tr>
</table>



---

# Content from pr-agent.1135329.md

# Text from pr-agent.1135329.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/31

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/fix/sync_perception_proto/mipilot/modules/perception_fusion/common/oracle/traj/traj_manager.cpp?ref_type=heads#L305-L309'><strong>代码异味</strong></a><br>在行305、307和309，`FusionState`枚举值的命名不一致。建议统一命名以提高代码可读性。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/fix/sync_perception_proto/mipilot/modules/L3/pnc/mimir/common/vehicle_manager/npc_manager.cpp?ref_type=heads#L90-L90'><strong>代码异味</strong></a><br>在行90，`FusionState`枚举值的命名不一致。建议统一命名以提高代码可读性。

</td></tr>
</table>



---

# Content from pr-agent.1124160.md

# Text from pr-agent.1124160.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/4

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/add_pnc/mipilot/proto/mipilot_proto_filepath.bzl?ref_type=heads#L386-L393'><strong>代码异味</strong></a><br>添加了大量新的proto文件，请确认这些文件是否都是必要的，并且是否有重复或冗余的内容。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/add_pnc/mipilot/proto/pilot/l3_pnc/planning.proto?ref_type=heads#L61-L62'><strong>可能的错误</strong></a><br>在`TrajectoryPoint`消息中，`wheel_torque_nm`字段被标记为“保留未来使用”，但未提供具体的未来用途说明。请确认这个字段是否真的需要，或者提供更多的上下文信息。

</td></tr>
</table>



---

# Content from pr-agent.1131354.md

# Text from pr-agent.1131354.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/17

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/change_port/docker_builder/launch_CLI_test.sh?ref_type=heads#L16-L22'><strong>可能的错误</strong></a><br>在行16和行19添加了新的节点启动命令，但在行22重新添加了之前移除的节点启动命令。请确认这些节点的启动顺序和依赖关系是否正确。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/feature/change_port/mipilot/conf/scripts/mipilot/scripts/mipilot-launch.sh?ref_type=heads#L135-L135'><strong>代码异味</strong></a><br>在行135注释掉了`exit 0`，这可能会导致脚本在`mipilot`已经启动时继续执行后续代码。请确认这是否是预期行为。

</td></tr>
</table>



---

# Content from pr-agent.1131170.md

# Text from pr-agent.1131170.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/16

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L85-L90'><strong>性能问题</strong></a><br>在`Process`函数中添加了时间测量代码，但未处理可能的异常情况。如果`std::chrono::high_resolution_clock::now()`失败，可能会导致程序崩溃。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L183-L184'><strong>代码异味</strong></a><br>在`CreateBboxObstacles`函数中，`ADS_INFO`日志的格式不一致。建议统一日志格式以提高可读性。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L310-L313'><strong>性能问题</strong></a><br>在`PreprocessAndDet`函数中添加了时间测量代码，但未处理可能的异常情况。如果`std::chrono::high_resolution_clock::now()`失败，可能会导致程序崩溃。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L325-L329'><strong>性能问题</strong></a><br>在`PreprocessAndDet`函数中添加了时间测量代码，但未处理可能的异常情况。如果`std::chrono::high_resolution_clock::now()`失败，可能会导致程序崩溃。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/tracking/bbox_obstacle_tracking_unit.cc?ref_type=heads#L66-L69'><strong>性能问题</strong></a><br>在`Process`函数中添加了时间测量代码，但未处理可能的异常情况。如果`std::chrono::high_resolution_clock::now()`失败，可能会导致程序崩溃。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/tracking/bbox_obstacle_tracking_unit.cc?ref_type=heads#L137-L140'><strong>性能问题</strong></a><br>在`Process`函数中添加了时间测量代码，但未处理可能的异常情况。如果`std::chrono::high_resolution_clock::now()`失败，可能会导致程序崩溃。

</td></tr>
</table>



---

# Content from pr-agent.1130960.md

# Text from pr-agent.1130960.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/15

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L85-L90'><strong>性能问题</strong></a><br>在`Process`函数中添加了时间计算和日志输出，可能会影响性能。请确认这些日志输出是否必要，并考虑在生产环境中移除。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L183-L183'><strong>代码异味</strong></a><br>在`CreateBboxObstacles`函数中，日志输出格式发生了变化。请确保日志输出格式一致，以便于调试和维护。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L312-L312'><strong>代码异味</strong></a><br>在`PreprocessAndDet`函数中，日志输出格式发生了变化。请确保日志输出格式一致，以便于调试和维护。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/detection/lidar_bbox_detection_preprocess_unit.cc?ref_type=heads#L325-L329'><strong>性能问题</strong></a><br>在`PreprocessAndDet`函数中添加了时间计算和日志输出，可能会影响性能。请确认这些日志输出是否必要，并考虑在生产环境中移除。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/tracking/bbox_obstacle_tracking_unit.cc?ref_type=heads#L66-L66'><strong>性能问题</strong></a><br>在`Process`函数中添加了时间计算和日志输出，可能会影响性能。请确认这些日志输出是否必要，并考虑在生产环境中移除。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/main/mipilot/modules/perception/common/lidar/tracking/bbox_obstacle_tracking_unit.cc?ref_type=heads#L137-L139'><strong>性能问题</strong></a><br>在`Process`函数中添加了时间计算和日志输出，可能会影响性能。请确认这些日志输出是否必要，并考虑在生产环境中移除。

</td></tr>
</table>



---

# Content from pr-agent.1123842.md

# Text from pr-agent.1123842.log,https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/merge_requests/2

## PR Reviewer Guide 🔍

<table>
<tr><td>⏱️&nbsp;<strong>Estimated effort to review</strong>: 3 🔵🔵🔵⚪⚪</td></tr>
<tr><td>🧪&nbsp;<strong>PR contains tests</strong></td></tr>
<tr><td>🔒&nbsp;<strong>Security concerns</strong><br><br>

否</td></tr>
<tr><td>⚡&nbsp;<strong>Key issues to review</strong><br><br>

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/prediction_dev/mipilot/modules/perception/modules/prediction/prediction_module.cc?ref_type=heads#L669-L676'><strong>可能的错误</strong></a><br>新增的UTM转换代码可能会导致性能问题，因为它在循环中调用了`TrajectoryPointFromVcsToUtm`方法。需要确保这个方法的性能足够高效。

<a href='https://git.n.xiaomi.com/l3-everyone/mipilot_rc08_l3/-/blob/prediction_dev/mipilot/modules/perception/common/prediction/executor_units/multipathpp/multipathpp_output_unit.cc?ref_type=heads#L325-L326'><strong>代码异味</strong></a><br>注释掉的代码行`point.set_spread_x(vcs_point.spread_x())`和`point.set_spread_y(vcs_point.spread_y())`可能是无用的，建议移除这些注释。

</td></tr>
</table>



---

