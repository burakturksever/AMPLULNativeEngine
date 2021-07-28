from engine.native_engine import NativeEngine

#
# Testing Python
#
code_string = """
print(3+5)
"""
ne = NativeEngine('LANG_P')
ne.native_run(code_string)
print(type(ne.get_output()))
print(ne.get_output())


#
# Testing C
#
c_code_string = """
#include <stdio.h>
int main(void) 
{
    printf("Hello, World! This is a C program that has been called using the NativeEngine");
    return(0);
}
"""
ne = NativeEngine("LANG_C")
ne.native_run(c_code_string)
print(type(ne.get_output()))
print(ne.get_output())


#
# Testing Java
#
j_code_string = """
public class HelloWorld {
    public static void main(String[] args) {
        double res = 3;
        res += 5.8;
        System.out.println(res);
    }
}
"""
ne = NativeEngine("LANG_J")
ne.native_run(j_code_string)
print(type(ne.get_output()))
print(ne.get_output())
