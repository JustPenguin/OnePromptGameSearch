"""Local file/workflow verification without changing research records."""
import argparse
import contextlib
import io
import json
import tempfile
from pathlib import Path
from types import SimpleNamespace
import manage

def main():
    original=manage.ROOT
    output=original/'validation'
    output.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='workflow-',dir=output) as folder:
        temporary=Path(folder).resolve()
        temporary.relative_to(output.resolve())
        manage.ROOT=temporary
        try:
            args=SimpleNamespace(name='Workflow Fixture',aliases=['Fixture Alias'],type='game',date='2026-10-06')
            with contextlib.redirect_stdout(io.StringIO()):manage.new_record(args)
            first=manage.records()[0]
            try:
                with contextlib.redirect_stdout(io.StringIO()):manage.new_record(args)
            except ValueError:duplicate_blocked=True
            else:duplicate_blocked=False
            for n in range(2,1001):
                r=dict(id=f'G{n:04d}',name=f'Synthetic fixture {n}',aliases=[],type='game',status='待核實',updated='2026-10-06',sources=[],sections=[])
                manage.write(temporary/f'records/G{n:04d}.md',manage.render_record(r,'Temporary verification data.\n'))
            rows=manage.rebuild()
            with contextlib.redirect_stdout(io.StringIO()):
                manage.new_record(SimpleNamespace(name='Next Fixture',aliases=[],type='game',date='2026-10-06'))
            last=manage.records()[-1]
            report=dict(existing_records_unchanged=True,fixture_record_count=len(rows),initial_id=first['id'],duplicate_name_blocked=duplicate_blocked,next_id_after_1000=last['id'],synthetic_data_not_in_research=True)
            assert len(rows)==1000 and duplicate_blocked and last['id']=='G1001'
            manage.write(output/'workflow-check.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        finally:
            manage.ROOT=original
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
