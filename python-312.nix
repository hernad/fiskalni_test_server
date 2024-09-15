{pkgs}:

pkgs.python312.withPackages (ps: [
    #ps.setuptools
    ps.fastapi
])

