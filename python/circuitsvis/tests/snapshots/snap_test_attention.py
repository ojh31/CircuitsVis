# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestAttention.test_matches_snapshot 1'] = '''<div id="circuits-vis-mock"/>
    <script crossorigin type="module">
    import { render, AttentionPatterns } from "https://unpkg.com/circuitsvis/dist/cdn/esm.js";
    render(
      "circuits-vis-mock",
      AttentionPatterns,
      {"tokens": ["a", "b"], "attention": [[[0, 1], [0, 1]]]}
    )
    </script>'''
