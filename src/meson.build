pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'passes')
gnome = import('gnome')

gnome.compile_resources('passes',
  'passes.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'passes.in',
  output: 'passes',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

passes_sources = [
  '__init__.py',
  'auxiliary/colored_box.py',
  'model/digital_pass.py',
  'model/digital_pass_factory.py',
  'model/persistence.py',
  'model/pkpass.py',
  'barcode_dialog.py',
  'barcode_widget.py',
  'main.py',
  'pkpass_back_view.py',
  'pkpass_field_row.py',
  'pkpass_front_view.py',
  'pkpass_row.py',
  'pkpass_row_header.py',
  'pkpass_view.py',
  'window.py',
]

install_data(passes_sources, install_dir: moduledir)
