from typing import Any, Dict, Optional

WORDING : Dict[str, Any] =\
{
	'conda_not_activated': '未激活Conda环境',
    'python_not_supported': 'Python版本不支持，请升级到{version}或更高版本',
    'ffmpeg_not_installed': '未安装FFMpeg',
    'creating_temp': '正在创建临时资源',
    'extracting_frames': '正在以{resolution}分辨率和每秒{fps}帧的速度提取帧',
    'extracting_frames_succeed': '提取帧成功',
    'extracting_frames_failed': '提取帧失败',
    'analysing': '正在分析',
    'processing': '正在处理',
    'downloading': '正在下载',
    'temp_frames_not_found': '未找到临时帧',
    'copying_image': '正在复制分辨率为{resolution}的图片',
    'copying_image_succeed': '复制图片成功',
    'copying_image_failed': '复制图片失败',
    'finalizing_image': '正在完成分辨率为{resolution}的图片',
    'finalizing_image_succeed': '完成图片成功',
    'finalizing_image_skipped': '跳过完成图片',
    'merging_video': '正在合并分辨率为{resolution}，每秒{fps}帧的视频',
    'merging_video_succeed': '合并视频成功',
    'merging_video_failed': '合并视频失败',
    'skipping_audio': '跳过音频',
    'restoring_audio_succeed': '恢复音频成功',
    'restoring_audio_skipped': '跳过恢复音频',
    'clearing_temp': '正在清除临时资源',
    'processing_stopped': '处理已停止',
    'processing_image_succeed': '图片处理成功，耗时{seconds}秒',
    'processing_image_failed': '图片处理失败',
    'processing_video_succeed': '视频处理成功，耗时{seconds}秒',
    'processing_video_failed': '视频处理失败',
    'model_download_not_done': '模型下载未完成',
    'model_file_not_present': '模型文件不存在',
    'select_image_source': '选择图片源路径',
    'select_audio_source': '选择音频源路径',
    'select_video_target': '选择视频目标路径',
    'select_image_or_video_target': '选择图片或视频目标路径',
    'select_file_or_directory_output': '选择输出文件或目录',
    'no_source_face_detected': '未检测到源人脸',
    'frame_processor_not_loaded': '帧处理器{frame_processor}无法加载',
    'frame_processor_not_implemented': '帧处理器{frame_processor}未正确实现',
    'ui_layout_not_loaded': '界面布局{ui_layout}无法加载',
    'ui_layout_not_implemented': '界面布局{ui_layout}未正确实现',
    'stream_not_loaded': '流{stream_mode}无法加载',
	'point': '.',
	'comma': ',',
	'colon': ':',
	'question_mark': '?',
	'exclamation_mark': '!',
	'help':
	{
		# installer
		'install_dependency': 'select the variant of {dependency} to install',
		'skip_conda': 'skip the conda environment check',
		# general
		'config': 'choose the config file to override defaults',
		'source': 'choose single or multiple source images or audios',
		'target': 'choose single target image or video',
		'output': 'specify the output file or directory',
		# misc
		'force_download': 'force automate downloads and exit',
		'skip_download': 'omit automate downloads and remote lookups',
		'headless': 'run the program without a user interface',
		'log_level': 'adjust the message severity displayed in the terminal',
		# execution
		'execution_device_id': 'specify the device used for processing',
		'execution_providers': 'accelerate the model inference using different providers (choices: {choices}, ...)',
		'execution_thread_count': 'specify the amount of parallel threads while processing',
		'execution_queue_count': 'specify the amount of frames each thread is processing',
		# memory
		'video_memory_strategy': 'balance fast frame processing and low VRAM usage',
		'system_memory_limit': 'limit the available RAM that can be used while processing',
		# face analyser
		'face_analyser_order': 'specify the order in which the face analyser detects faces',
		'face_analyser_age': 'filter the detected faces based on their age',
		'face_analyser_gender': 'filter the detected faces based on their gender',
		'face_detector_model': 'choose the model responsible for detecting the face',
		'face_detector_size': 'specify the size of the frame provided to the face detector',
		'face_detector_score': 'filter the detected faces base on the confidence score',
		'face_landmarker_score': 'filter the detected landmarks base on the confidence score',
		# face selector
		'face_selector_mode': 'use reference based tracking or simple matching',
		'reference_face_position': 'specify the position used to create the reference face',
		'reference_face_distance': 'specify the desired similarity between the reference face and target face',
		'reference_frame_number': 'specify the frame used to create the reference face',
		# face mask
		'face_mask_types': 'mix and match different face mask types (choices: {choices})',
		'face_mask_blur': 'specify the degree of blur applied the box mask',
		'face_mask_padding': 'apply top, right, bottom and left padding to the box mask',
		'face_mask_regions': 'choose the facial features used for the region mask (choices: {choices})',
		# frame extraction
		'trim_frame_start': 'specify the the start frame of the target video',
		'trim_frame_end': 'specify the the end frame of the target video',
		'temp_frame_format': 'specify the temporary resources format',
		'keep_temp': 'keep the temporary resources after processing',
		# output creation
		'output_image_quality': 'specify the image quality which translates to the compression factor',
		'output_image_resolution': 'specify the image output resolution based on the target image',
		'output_video_encoder': 'specify the encoder use for the video compression',
		'output_video_preset': 'balance fast video processing and video file size',
		'output_video_quality': 'specify the video quality which translates to the compression factor',
		'output_video_resolution': 'specify the video output resolution based on the target video',
		'output_video_fps': 'specify the video output fps based on the target video',
		'skip_audio': 'omit the audio from the target video',
		# frame processors
		'frame_processors': 'load a single or multiple frame processors. (choices: {choices}, ...)',
		'face_debugger_items': 'load a single or multiple frame processors (choices: {choices})',
		'face_enhancer_model': 'choose the model responsible for enhancing the face',
		'face_enhancer_blend': 'blend the enhanced into the previous face',
		'face_swapper_model': 'choose the model responsible for swapping the face',
		'frame_colorizer_model': 'choose the model responsible for colorizing the frame',
		'frame_colorizer_blend': 'blend the colorized into the previous frame',
		'frame_colorizer_size': 'specify the size of the frame provided to the frame colorizer',
		'frame_enhancer_model': 'choose the model responsible for enhancing the frame',
		'frame_enhancer_blend': 'blend the enhanced into the previous frame',
		'lip_syncer_model': 'choose the model responsible for syncing the lips',
		# uis
		'open_browser': 'open the browser once the program is ready',
		'ui_layouts': 'launch a single or multiple UI layouts (choices: {choices}, ...)'
	},
	'uis':
	{
		# general
		'start_button': '开始',
		'stop_button': '停止',
		'clear_button': '清除',
		# about
		'donate_button': '大灰狼自用专版',
		# benchmark
		'benchmark_results_dataframe': '基准测试结果',
		# benchmark options
		'benchmark_runs_checkbox_group': '基准测试运行次数',
		'benchmark_cycles_slider': '基准测试周期',
		# common options
		'common_options_checkbox_group': '选项',
		# execution
		'execution_providers_checkbox_group': '执行提供者',
		# execution queue count
		'execution_queue_count_slider': '执行队列数量',
		# execution thread count
		'execution_thread_count_slider': '执行线程数量',
		# face analyser
		'face_analyser_order_dropdown': '人脸分析器顺序',
		'face_analyser_age_dropdown': '人脸分析器年龄',
		'face_analyser_gender_dropdown': '人脸分析器性别',
		'face_detector_model_dropdown': '人脸检测器模型',
		'face_detector_size_dropdown': '人脸检测器尺寸',
		'face_detector_score_slider': '人脸检测器得分',
		'face_landmarker_score_slider': '人脸标记器得分',
		# face masker
		'face_mask_types_checkbox_group': '人脸遮罩类型',
		'face_mask_blur_slider': '人脸遮罩模糊度',
		'face_mask_padding_top_slider': '人脸遮罩顶部填充',
		'face_mask_padding_right_slider': '人脸遮罩右侧填充',
		'face_mask_padding_bottom_slider': '人脸遮罩底部填充',
		'face_mask_padding_left_slider': '人脸遮罩左侧填充',
		'face_mask_region_checkbox_group': '人脸遮罩区域',
		# face selector
		'face_selector_mode_dropdown': '人脸选择器模式',
		'reference_face_gallery': '参考人脸库',
		'reference_face_distance_slider': '参考人脸相似度',
		# frame processors
		'frame_processors_checkbox_group': '帧处理器',
		# frame processors options
		'face_debugger_items_checkbox_group': '人脸调试项目',
		'face_enhancer_model_dropdown': '人脸增强器模型',
		'face_enhancer_blend_slider': '人脸增强器混合度',
		'face_swapper_model_dropdown': '人脸交换器模型',
		'frame_colorizer_model_dropdown': '帧着色器模型',
		'frame_colorizer_blend_slider': '帧着色器混合度',
		'frame_colorizer_size_dropdown': '帧着色器尺寸',
		'frame_enhancer_model_dropdown': '帧增强器模型',
		'frame_enhancer_blend_slider': '帧增强器混合度',
		'lip_syncer_model_dropdown': '唇形同步器模型',
		# memory
		'video_memory_strategy_dropdown': '视频内存策略',
		'system_memory_limit_slider': '系统内存限制',
		# output
		'output_image_or_video': '输出',
		# output options
		'output_path_textbox': '输出路径',
		'output_image_quality_slider': '输出图像质量',
		'output_image_resolution_dropdown': '输出图像分辨率',
		'output_video_encoder_dropdown': '输出视频编码器',
		'output_video_preset_dropdown': '输出视频预设',
		'output_video_quality_slider': '输出视频质量',
		'output_video_resolution_dropdown': '输出视频分辨率',
		'output_video_fps_slider': '输出视频帧率',
		# preview
		'preview_image': '预览',
		'preview_frame_slider': '预览帧',
		# source
		'source_file': '源文件',
		# target
		'target_file': '目标文件',
		# temp frame
		'temp_frame_format_dropdown': '临时帧格式',
		# trim frame
		'trim_frame_start_slider': '裁剪帧开始',
		'trim_frame_end_slider': '裁剪帧结束',
		# webcam
		'webcam_image': '网络摄像头',
		# webcam options
		'webcam_mode_radio': '网络摄像头模式',
		'webcam_resolution_dropdown': '网络摄像头分辨率',
		'webcam_fps_slider': '网络摄像头帧率'
	}
}


def get(key : str) -> Optional[str]:
	if '.' in key:
		section, name = key.split('.')
		if section in WORDING and name in WORDING[section]:
			return WORDING[section][name]
	if key in WORDING:
		return WORDING[key]
	return None
