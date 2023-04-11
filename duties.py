from duty import duty


@duty
def format(ctx):
    ctx.run("ruff kz_iin_validator/ tests/ duties.py --fix", title="Formating code")
