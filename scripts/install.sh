WORKPLACE="$HOME/workplace"

(
  cd "$WORKPLACE/PythonUtils"
  pip install .
  rm -rf build
)
