#!/usr/bin/python3
"""The `__init__` module turns our `models` to a package.
This also implements an effective storage system by updating
the `FileStorage` whenever any module included in the `models`
package is being imported or used anywhere.
A `storage` instance/object is always instantiated whenever any
module in `models` package is being imported or used."""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
