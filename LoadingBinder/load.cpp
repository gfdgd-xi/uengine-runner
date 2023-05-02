#include <iostream>
using namespace std;
int main(){
    // 检查是否是 root 用户
    if(system("[[ `whoami` == root ]]")){
        cout << "这不是 root 账户，失败！";
        return 1;
    }
    system("modprobe binder_linux");
    system("mkdir /dev/binderfs");
    system("mount -t binder binder /dev/binderfs");
    return 0;
}