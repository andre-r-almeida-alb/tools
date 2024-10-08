#!/bin/sh

java_version=$1
java_home=

IFS=$'\n'
for d in $(find "/c/Program Files/Java" -name "jdk*$java_version*" -type d); do
    java_home="$d"
done

if [ -z "$java_home" ]; then
    echo "Could not find Java version $java_version"
else
    export JAVA_HOME="$java_home"
    export PATH="$java_home/bin:$PATH"
    echo "Activated Java version $java_version ($java_home)"
fi