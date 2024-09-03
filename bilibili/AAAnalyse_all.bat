@echo off
chcp 65001  > nul 2>&1

echo 按任意键开始分析,分析时间可能较长耐心等待，输出结果将自动保存成log！！！
pause
md "..\output"
..\..\venv\Scripts\python.exe mergeJson.py >..\output\output.log 2>&1
echo 正在进行下一项
..\..\venv\Scripts\python.exe analyse_activeViewer.py >>..\output\output.log 2>&1
echo 正在进行下一项
..\..\venv\Scripts\python.exe analyse_cloud.py >>..\output\output.log 2>&1
echo 正在进行下一项
..\..\venv\Scripts\python.exe analyse_time_long.py >>..\output\output.log 2>&1
echo 正在进行下一项
..\..\venv\Scripts\python.exe analyse_video_Popularity.py >>..\output\output.log 2>&1
echo 正在进行下一项
..\..\venv\Scripts\python.exe analyse_video_Heat.py >>..\output\output.log 2>&1
echo 正在进行下一项
..\..\venv\Scripts\python.exe analyse_api_SentimentIntensity.py >>..\output\output.log 2>&1
echo 正在进行下一项
..\..\venv\Scripts\python.exe analyse_situation.py >>..\output\output.log 2>&1
echo 分析完毕！
pause
