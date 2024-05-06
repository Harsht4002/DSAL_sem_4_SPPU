#include <iostream>
#include <string>
#include <fstream>
using namespace std;
struct node{
    int rno;
    string name;
    char division;
};
void createfile(){
    ofstream f;
    f.open("students.txt");
    if(!f){
        cout<<"failed to open"<<endl;
        return;
    }
    f.close();
}
void add(){
    ofstream f;
    f.open("students.txt",ios::app);
    if(!f){
        cout<<"failed to open"<<endl;
        return;
    }
    node s;
    cout<<"enter rno of student"<<endl;
    cin>>s.rno;
    cout<<"enter name of student"<<endl;
    cin>>s.name;
    cout<<"enter division"<<endl;
    cin>>s.division;
    f<<s.rno<<" "<<s.name<<" "<<s.division<<" "<<endl;
    f.close();
}
void display(){
    ifstream inf;
    inf.open("students.txt");
    if(!inf){
        cout<<"failed to open"<<endl;
        return;
    }
    node n;
    while(inf>> n.rno >> n.name >> n.division){
        cout<<"name: "<<n.name<<" "<<"rno: "<<n.rno<<"division: "<<n.division<<endl;
    }
    inf.close();
}
void searchandremove(int r){
    ifstream inf;
    ofstream temp;
    inf.open("students.txt");
    temp.open("temp.txt");
     if (!inf || !temp) {
        cout<< " Error opening files." << endl;
        return;
    }
    node n;
    bool found=false;
    while(inf>>n.rno>>n.name>>n.division){
        if(n.rno!=r){
            temp<<n.rno<<" "<<n.name<<" "<<n.division<<endl;
        }
        else{
            found=true;
            cout<<" found roll number: "<<n.rno<<" name: "<<n.name<<" division: "<<n.division<<endl;
        }
    }
    inf.close();
    temp.close();
    remove("students.txt");
    rename("temp.txt","students.txt");
    if(found==false){
        cout<<"not found"<<endl;
    }
}
int main(){
    int ch;
    do{
        cout<<" 1.create file"<<endl<<" 2.add student"<<endl<<" 3.display"<<endl<<"4.seacrhandremove"<<endl<<"5.exit"<<endl;
        cin>>ch;
        switch(ch){
            case 1:
            createfile();
            break;
            case 2:
            add();
            break;
            case 3:
            display();
            break;
            case 4:
            int r;
            cout<<"enter roll number to search and remove: "<<endl;
            cin>>r;
            searchandremove(r);
        }
    }while(ch<5&&ch>0);
    return 0;
}
