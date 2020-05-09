'`matflow_formable.__init__.py`'

from functools import partial

from matflow_formable._version import __version__

from matflow import (
    input_mapper,
    output_mapper,
    cli_format_mapper,
    register_output_file,
    func_mapper,
)

input_mapper = partial(input_mapper, software='formable')
output_mapper = partial(output_mapper, software='formable')
cli_format_mapper = partial(cli_format_mapper, software='formable')
register_output_file = partial(register_output_file, software='formable')
func_mapper = partial(func_mapper, software='formable')

# This import must come after assigning the partial functions:
from matflow_formable import main
from matflow_formable import load