# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestRenderProd.test_example_element 1'] = '''<div id="circuits-vis-mock"/>
    <script crossorigin type="module">
    import { render, Hello } from "https://unpkg.com/circuitsvis/dist/cdn/esm.js";
    render(
      "circuits-vis-mock",
      Hello,
      {"name": "Bob"}
    )
    </script>'''
