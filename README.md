# Video_Streaming_with_Flask/基于Flask的实时视频流传输
代码为以下博客的实践与改编
https://blog.miguelgrinberg.com/post/video-streaming-with-flask



只是一个简单的demo

- 已经解决的问题：

	1. 通过`host`参数实现主机访问VMware虚拟机

	1. Ubuntu1604浏览器无法正常显示监控(app.run里关闭调试模式，或者设置use_reloader = False即可)
	1.播放本地视频报错`Assertion fctx->async_lock failed at libavcodec/pthread_frame.c:155`

- 待解决问题：

	1. 多任务并发时掉帧严重
	
	1. OpenCV直接传输视频流，而无需经过jpeg转换
