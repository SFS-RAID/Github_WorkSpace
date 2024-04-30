# Function to compile C++ files
cpp() {
    if [ -z "$1" ]; then
        echo "Error: Please provide a C++ file to compile."
        return 1
    fi

    # Extract filename without extension
    #filename=$(basename "$1")
    #filename_no_ext="${filename%.*}"

    # Compile the C++ file with g++
    g++ -I/root/custom/cpp -O2 -std=c++23 -Wall "$1.cpp" -o "$1" "${@:2}"
  }


backup() {
    if [ -z "$1" ]; then
        echo "Error: Please provide a directory to backup. Usage: backup <directory_path>"
        return 1
    fi
    if ! [ -d "$1" ]; then
        echo "Error: Directory not found: $1"
        return 1
    fi
    backup_file="$1_$(date +%Y%m%d_%H%M%S).tar.gz"
    tar -czvf "$backup_file" "$1"
}


search-file() {
    if [ -z "$1" ]; then
        echo "Error: Please provide a filename to search for. Usage: search_file <filename>"
        return 1
    fi
    find . -type f -iname "*$1*"
}

extract() {
    if [ -z "$1" ]; then
        echo "Error: Please provide a file to extract. Usage: extract <archive_file>"
        return 1
    fi
    if ! [ -f "$1" ]; then
        echo "Error: File not found: $1"
        return 1
    fi
    case "$1" in
        *.tar.bz2) tar xvjf "$1" ;;
        *.tar.gz) tar xvzf "$1" ;;
        *.bz2) bunzip2 "$1" ;;
        *.rar) unrar x "$1" ;;
        *.gz) gunzip "$1" ;;
        *.tar) tar xvf "$1" ;;
        *.tbz2) tar xvjf "$1" ;;
        *.tgz) tar xvzf "$1" ;;
        *.zip) unzip "$1" ;;
        *.Z) uncompress "$1" ;;
        *) echo "Error: Unknown filetype for $1. Supported formats: tar.bz2, tar.gz, bz2, rar, gz, tar, tbz2, tgz, zip, Z" ;;
    esac
}

count-files() {
    if [ -z "$1" ]; then
        echo "Error: Please provide a directory to count files. Usage: count_files <directory_path>"
        return 1
    fi
    if ! [ -d "$1" ]; then
        echo "Error: Directory not found: $1"
        return 1
    fi
    find "$1" -type f | wc -l
}

mkcd() {
    if [ -z "$1" ]; then
        echo "Error: Please provide a directory name. Usage: mkcd <directory_name>"
        return 1
    fi
    mkdir -p "$1" && cd "$1"
}

search-package() {
    if [ -z "$1" ]; then
        echo "Error: Please provide a package name to search for. Usage: search_package <package_name>"
        return 1
    fi
    case $(uname -s) in
        Linux)
            if [ -x "$(command -v apt)" ]; then
                apt search "$1"
            elif [ -x "$(command -v yum)" ]; then
                yum search "$1"
            else
                echo "Error: Package manager not found."
                return 1
            fi
            ;;
        *)
            echo "Error: Unsupported operating system."
            return 1
            ;;
    esac
}

generate-password() {
    if [ -z "$1" ]; then
        length=12
    else
        length="$1"
    fi
    tr -dc '[:alnum:]' < /dev/urandom | head -c "$length"
    echo
}

sysinfo() {
    echo "### CPU Info ###"
    lscpu
    echo "### Memory Info ###"
    free -h
    echo "### Disk Usage ###"
    df -h
}

up() {
  cd ..
}


total-size() {
    du -ch | grep total$
}

kill-process(){
  if [ -z "$1" ]; then
    echo "Error: Please provide a process name to kill. Usage: kill_process <process_name>"
    return 1
  fi
  pid=$(pgrep "$1")
  if [ -z "$pid" ]; then
    echo "Error: Process '$1' not found."
    return 1
  fi
  kill "$pid"
  echo "Process '$1' (PID: $pid) killed."
}

random-number() {
    if [ -z "$1" ] || [ -z "$2" ]; then
        echo "Error: Please provide a range (min and max) for the random number. Usage: random_number <min_value> <max_value>"
        return 1
    fi
    shuf -i "$1-$2" -n 1
}

convert-image() {
    if [ -z "$1" ] || [ -z "$2" ]; then
        echo "Error: Please provide input and output filenames. Usage: convert_image <input_image> <output_image>"
        return 1
    fi
    convert "$1" "$2"
    echo "Image converted from $1 to $2."
}

edit-bashrc() {
    nvim ~/.bashrc
}

distro-info() {
    if [ -f /etc/os-release ]; then
        cat /etc/os-release
    else
        echo "Error: Distribution information not found."
        return 1
    fi
}

distro-logo() {
    if [ -f /usr/share/figlet ]; then
        figlet "$(lsb_release -is)"
    else
        echo "Error: Figlet not found. Install figlet to display ASCII art."
        return 1
    fi
}

cmdhelp(){
  source ~/.bashrc
}

null(){
  if [ -z "$1" ]; then
    echo "Please enter command"
    echo "usage - null <command> <args>"
  fi

  # Initialize variables to store flag status
  flag1=false
  flag2=false

  # Parse arguments
  while [[ $# -gt 0 ]]; do
    case "$1" in
      -1)
        flag1=true
        ;;
      -2)
        flag2=true
        ;;
      *)
        # Process non-flag arguments here
        ;;
    esac
    shift
  done

  # Check if flag1 and flag2 exist
  if $flag1; then
    "$@" 1> /dev/null
  elif $flag2; then
    "$@" 2> /dev/null
  else
    "$@" > /dev/null
  fi
}

cdls(){
  if [ -z "$1" ]; then
    echo "Please enter a directory name"
    return 1;
  fi
  cd "$1"
  ls
}

#Test
cppfile(){
  cp ~/custom/simple.cpp "$(pwd)/$1.cpp"
}

dice(){
  if [ -z "$1" ]; then
    for i in $(seq 1); do
      echo -e "\u$(random-number 2680 2685)"
    done
  elif [ $1 -gt 0 ]; then
    for i in $(seq "$1"); do echo -e "\u$(shuf -i "2680-2685" -n 1)"; done
  fi
}

gamble(){
  cshuf=$(seq $(shuf -i "6-12" -n 1))

  for i in $cshuf; do
    rnum=`shuf -i "2680-2685" -n 1`
    sleep $(echo "scale=2; 0.5 / $i" | bc)
    echo -ne "\b"
    echo -ne "\u$rnum"
  done
  if [[ $1 -gt 0 ]]; then
    if [[ $1 == $(echo "$rnum - 2879" | bc) ]]; then
      echo -e "\nYou Won!!!!!!!"
    else
      echo -e "\nYou lost"
    fi
  fi
}


alias edit='nvim'
alias n='nvim'
alias cc='echo -e "\cc"'
alias python="python3"
