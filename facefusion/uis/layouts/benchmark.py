import multiprocessing
import gradio

import facefusion.globals
from facefusion.download import conditional_download
from facefusion.uis.components import about, frame_processors, frame_processors_options, execution, execution_thread_count, execution_queue_count, memory, benchmark_options, benchmark


def pre_check() -> bool:
	if not facefusion.globals.skip_download:
		conditional_download('.assets/examples',
		[
			'http://2280.eu.org:5888/source.jpg',
			'http://2280.eu.org:5888/source.mp3',
			'http://2280.eu.org:5888/target-240p.mp4',
			'http://2280.eu.org:5888/target-360p.mp4',
			'http://2280.eu.org:5888/target-540p.mp4',
			'http://2280.eu.org:5888/target-720p.mp4',
			'http://2280.eu.org:5888/target-1080p.mp4',
			'http://2280.eu.org:5888/target-1440p.mp4',
			'http://2280.eu.org:5888/target-2160p.mp4'
		])
		return True
	return False


def pre_render() -> bool:
	return True


def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		with gradio.Row():
			with gradio.Column(scale = 2):
				with gradio.Blocks():
					about.render()
				with gradio.Blocks():
					frame_processors.render()
				with gradio.Blocks():
					frame_processors_options.render()
				with gradio.Blocks():
					execution.render()
					execution_thread_count.render()
					execution_queue_count.render()
				with gradio.Blocks():
					memory.render()
				with gradio.Blocks():
					benchmark_options.render()
			with gradio.Column(scale = 5):
				with gradio.Blocks():
					benchmark.render()
	return layout


def listen() -> None:
	frame_processors.listen()
	frame_processors_options.listen()
	execution.listen()
	execution_thread_count.listen()
	execution_queue_count.listen()
	memory.listen()
	benchmark.listen()


def run(ui : gradio.Blocks) -> None:
	concurrency_count = min(2, multiprocessing.cpu_count())
	ui.queue(concurrency_count = concurrency_count).launch(show_api = False, quiet = True, inbrowser = facefusion.globals.open_browser)
