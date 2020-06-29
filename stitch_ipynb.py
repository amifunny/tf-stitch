def stitch_notebook( temp_blocks ):

    cells = []

    for block in temp_blocks:
      
        cell_type = 'code'

        cell = {
            'cell_type': cell_type,
            'metadata': {},
            # 'source': block,
            'source': block.splitlines(True),
            'outputs': [], 
            'execution_count': None
        }

        cells.append(cell)

    notebook = {
        'nbformat': 4,
        'nbformat_minor': 0,
        'metadata': {
            'anaconda-cloud': {},
            'kernelspec': {
                'display_name': 'Python 3',
                'language': 'python',
                'name': 'python3'},
            'language_info': {
                'codemirror_mode': {'name': 'ipython', 'version': 3},
                'file_extension': '.py',
                'mimetype': 'text/x-python',
                'name': 'python',
                'nbconvert_exporter': 'python',
                'pygments_lexer': 'ipython3',
                'version': '3.6.1'}
        },
        'cells': cells,
    }

    return notebook


