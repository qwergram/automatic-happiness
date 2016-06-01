# This script reads JeliumBot.java and reads all the class names and executes them
# via "java $classname"

clean() {
  # remove existing .class files
  current_classes="`ls | grep .class`"
  for class in $(echo $current_classes | tr "" " ")
  do
    rm $class
  done
}

compile_and_execute() {
  file_name="JeliumBot.java"
  javac $file_name
  if [ $? == 0 ]; then
    classes="`cat $file_name | grep class`"
    last=""
    for word in $(echo $classes | tr "\n" ";")
    do
      if [ "$last" == "class" ]; then
        java $word
      fi
      last=$word
    done
  fi
}

clean
compile_and_execute
