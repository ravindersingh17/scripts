#!/usr/bin/env bash

ADB=$(which adb)
alias sshphone="ssh -p 8022 u0_a110@192.168.43.1"

sshrootphone() {
	ssh -p 8022 u0_a117@$1
}

removeapp() {
	if [ "Success" !=  "$($ADB shell pm uninstall $1)" ]; then
		adb shell pm uninstall -k --user 0 $1
		echo "Only User uninstall possible"
	else
		echo "System Uninstall done"
	fi
}

appinfo() {
	adb shell dumpsys package $1
}

removeappuser() {
	adb shell pm uninstall -k --user 0 $1
}

searchapp() {
	adb shell pm list packages -f | grep $1
}

listapps() {
	adb shell pm list packages -f
}

pushfile() {
	adb push $1 sdcard/Download/
}

pullfile() {
	adb pull $1
}

installapk() {
	adb install $1
}
export JACK_SERVER_VM_ARGUMENTS="-Dfile.encoding=UTF-8 -XX:+TieredCompilation -Xmx1536m"
