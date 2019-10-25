// ==UserScript==
// @name         TubeNinja
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  download video and audio
// @author       DavidDay
// @include      http://*
// @include      https://*
// @grant        GM_registerMenuCommand
// ==/UserScript==

(function() {
    'use strict';
    var $ = $ || window.$;

	var window_url = window.location.href;
    var website_host = window.location.host;
    //脚本只运行在顶层窗口
    if (window.top != window.self){
    	return;
	}

    var download = {};
    download.start = function(){
        if (window.location.href.indexOf('tubeninja.net') > -1)
        {
            alert('Open video/audio and then click the button...');
        } else
        {
            open('http://www.tubeninja.net/?url='+encodeURIComponent(window.location.href)+'&utm_source=bookmarklet&utm_medium=redirect');
        }
    }

    GM_registerMenuCommand("download any video",function(){
            	download.start();
            });
})();