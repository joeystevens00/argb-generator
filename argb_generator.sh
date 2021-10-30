docker build . -t argb_generator
touch .argb_state
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

docker run -v "$SCRIPT_DIR/.argb_state:/home/app/code/.argb_state" argb_generator
