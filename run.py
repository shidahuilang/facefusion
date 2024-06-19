#!/usr/bin/env python3

import os
from facefusion import core
from rich.console import Console
from rich.progress import track
import time

console = Console()

def display_startup_info():
    os.system('title 大灰狼-FaceFusion 启动脚本')  # 设置控制台标题
    console.print("[bold yellow]大灰狼-FaceFusion[/bold yellow]")
    console.print("[bold yellow]版本: v2.6.1[/bold yellow]\n")
    console.print("[bold green]启动中...请稍等[/bold green]\n")
    for step in track(range(10), description="处理进度"):
        time.sleep(0.1)  # 模拟处理过程

if __name__ == '__main__':
    display_startup_info()
    core.cli()
