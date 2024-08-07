S_RED='\033[0;31m'
S_GRAY='\033[0;90m'

# Display ASCII art at startup
echo -e "${S_RED}###############################################"
echo -e "${S_GRAY}Custom Commands ${S_RED}"
echo -e "${S_GRAY}cpp (file w/0 ext) compile files${S_RED}"
echo -e "${S_GRAY}backup <directory_path>${S_RED}"
echo -e "${S_GRAY}search-file <filename>${S_RED}"
echo -e "${S_GRAY}extract <archive_file>${S_RED}"
echo -e "${S_GRAY}count-files <directory_path>${S_RED}"
echo -e "${S_GRAY}mkcd <directory_name>${S_RED}"
echo -e "${S_GRAY}search-package <package_name>${S_RED}"
echo -e "${S_GRAY}generate-password [length]${S_RED}"
echo -e "${S_GRAY}sysinfo${S_RED}"
echo -e "${S_GRAY}up${S_RED}"
echo -e "${S_GRAY}total-size${S_RED}"
echo -e "${S_GRAY}kill-process <process_name>${S_RED}"
echo -e "${S_GRAY}random-number <min_value> <max_value>${S_RED}"
echo -e "${S_GRAY}convert-image <input_image> <output_image>${S_RED}"
echo -e "${S_GRAY}edit-file <filename>${S_RED}"
echo -e "${S_GRAY}edit_bashrc${S_RED}"
echo -e "${S_GRAY}distro-info${S_RED}"
echo -e "${S_GRAY}distro-logo${S_RED}"
echo -e "${S_GRAY}cdls${S_RED}"
echo -e "${S_GRAY}n, edit - open nvim${S_RED}"
echo -e "${S_GRAY}cppfile <name>- Create a CPP template in Current folder${S_RED}"
echo -e "${S_GRAY}null <command> <args> - runs command without output -1 for error only and -2 for output only, no flags for both${S_RED}"
echo -e "${S_GRAY}steghide embed/extract -ef \[secret] -cf \[cover] -p [\"password\"]${S_RED}"
echo -e "${S_GRAY}dice [tries]- roll a dice${S_RED}"
echo -e "${S_GRAY}writeh fast/normal/slow \"text\" - Display text one by one like a human typing${S_RED}"
echo -e "\n"

echo -e "${S_GRAY}cmdhelp - LIST ALL COMMANDS${S_RED}"
echo -e "${S_RED}###############################################"
