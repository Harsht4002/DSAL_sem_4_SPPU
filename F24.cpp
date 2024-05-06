#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;
struct employee{
    int id;
    string name;
};
struct index{
    int id;
    int position;
};
void addemployee(vector<index>& vectorindex){
    ofstream outf;
    outf.open("sample.txt",ios::app);
    int offset=outf.tellp();
    employee e1;
    cout<<"enter name: "<<endl;
    cin>>e1.name;
    cout<<"enter id: "<<endl;
    cin>>e1.id;
    outf<<e1.id<<" "<<e1.name<<endl;
    index i1;
    i1.id=e1.id;
    i1.position=offset;
    vectorindex.push_back(i1);
    outf.close();
}
void displayemployee(){
    
    ifstream inf;
    inf.open("sample.txt");
    if(!inf){
        cout<<"failed to open"<<endl;
        return;
    }
    employee e1;
    while(inf>> e1.id>> e1.name ){
        cout<<"name: "<<e1.name<<" "<<"id: "<<e1.id<<endl;
    }
    inf.close();
}
void search(vector<index>& v1,int id1){
    int pos;
    bool found;
    for(auto it:v1){
        if(it.id==id1){
            pos=it.position;
            found=true;
            break;
        }
    }
    if(found==true){
    ifstream inf;
    inf.open("sample.txt",ios::in);
    inf.seekg(pos);
    string line;
    getline(inf,line);
    cout<<"found: "<<line<<endl;
    inf.close();
    return;
    }
    else{
        cout<<"not found"<<endl;
        return;
    }
}
void deleteemployee(vector<index>& v1,int id1){
    int j=0;
    bool found;
    for(auto it:v1){
        if(it.id==id1){
            j++;
            found=true;
            break;
        }
    }
    if(found==false){
        cout<<"not found"<<endl;
        return;
    }
    v1.erase(v1.begin()+j);
    ifstream inf;
    inf.open("sample.txt",ios::in);
    ofstream temp;
    temp.open("temp.txt",ios::out);
    for(int i=0;i<v1.size();i++){
    int pos=v1[i].position;
    inf.seekg(pos);
    string line;
    getline(inf,line);
    temp<<line<<endl;
    }
    inf.close();
    temp.close();
    remove("sample.txt");
    rename("temp.txt","sample.txt");
}
int main()
{
   vector<index> v1;
   addemployee(v1);
   addemployee(v1);
   displayemployee();
   search(v1,101);
   deleteemployee(v1,101);
   return 0;
}
