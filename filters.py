#!/usr/bin/env python
# -*- coding: utf-8 -*-
# define filers used in theme

from liquidluck.utils import to_datetime


def tagsize(value):
	from math import log

	if isinstance(value, int):
		return 100 + log(value or 1) * 20
	else:
		return value


def gravatar_url(email, size=16):
	"""
	generate URL requiered to request a Gravatar Image
	using gravatar variable in theme.vars of the setting file:
	gravatar: your gravatar email address
	"""
	from hashlib import md5
	from urllib import urlencode

	gravatar_url = "http://www.gravatar.com/avatar/" + md5(email.lower()).hexdigest() + "?"
	return gravatar_url + urlencode({'s':str(size)})


def parse_content(value, toc):
	import re

	def transform_videolink(value):
		# www.youku.com / 优酷
		value = re.sub(
			r'<a href="http://v.youku.com/v_show/id_([a-zA-Z0-9\=]+).html">',
			r'<iframe height=498 width=510 frameborder=0 allowfullscreen src='
			r'"http://player.youku.com/embed/\1"></iframe>'
			r'<a rel="nofollow" href="http://v.youku.com/v_show/id_\1.html">',
			value)

		# www.tudou.com / 土豆
		value = re.sub(
			r'<a href="http://www.tudou.com/programs/view/([a-zA-z0-9\-\=\_]+)/">',
			r'<embed src="http://www.tudou.com/v/\1/v.swf" '
			r'type="application/x-shockwave-flash" allowscriptaccess="always" '
			r'allowfullscreen="true" wmode="opaque" width="480" height="400"><br />'
			r'<a rel="nofollow" href="http://www.tudou.com/programs/view/\1/">',
			value)

		# www.yinyuetai.com / 音悦台
		value = re.sub(
			r'<a href="http://www.yinyuetai.com/video/(\d+)">',
			r'<embed src="http://www.yinyuetai.com/video/player/\1/v_0.swf" '
			r'quality="high" width="480" height="334" align="middle" allowScriptAccess="sameDomain" '
			r'allowfullscreen="true" type="application/x-shockwave-flash"><br />'
			r'<a rel="nofollow" href="http://www.yinyuetai.com/video/\1">',
			value)

		return value


	def parse_toc(value, toc):
		# parse table of contents [TOC]
		if toc:
			toc = unicode(toc)
			toc = re.sub(r'<sup class="footnote-ref(.*?)</sup>', '', toc) # strip footnote links
			value = value.replace('<p>[TOC]</p>', '<div class="toc">%s</div>' % toc)

		return value


	def parse_github(value):
		value = re.sub(
			r'([a-zA-Z0-9]+/[a-zA-Z0-9_\-]+@[a-fA-F0-9]{7})',
			r'<span class="btn icon-github icon-large">\1</span>',
			value)

		return value

	value = transform_videolink(value)
	value = parse_github(value)
	return parse_toc(value, toc)