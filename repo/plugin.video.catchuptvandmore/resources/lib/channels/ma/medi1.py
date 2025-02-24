# -*- coding: utf-8 -*-
# Copyright: (c) 2017, SylvainCecchetto
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)

# This file is part of Catch-up TV & More

from __future__ import unicode_literals
import re
import urlquick

# noinspection PyUnresolvedReferences
from codequick import Resolver

from resources.lib import resolver_proxy, web_utils

URL_LIVES = 'https://idara.medi1tv.ma/rss/embed/medi1news-auto/live-medi1tv-%s.aspx'

GENERIC_HEADERS = {"User-Agent": web_utils.get_random_ua()}


@Resolver.register
def get_live_url(plugin, item_id, **kwargs):

    resp = urlquick.get(URL_LIVES % item_id, headers=GENERIC_HEADERS, max_age=-1)
    video_url = 'https:' + re.compile(r"file: \'(.*?)\'").findall(resp.text)[0]

    return resolver_proxy.get_stream_with_quality(plugin, video_url)
