let task_list = [];
const button_add = document.querySelector("#add-task-button");

function load_local_storage(){
    let task_list = JSON.parse(localStorage.getItem("tasks")) || [];
    task_list.forEach((task) =>{
        let tag_li = create_li();
        tag_li.childNodes[1].innerHTML = task;
        document.querySelector('#task-list').appendChild(tag_li);
    });
}
load_local_storage();

button_add.addEventListener('click',(e) =>{
    const task_input = document.querySelector("#input-task");
    if(task_input.value !== ""){
        let tag_li = create_li();
        tag_li.childNodes[1].innerHTML = task_input.value;
        document.querySelector('#task-list').appendChild(tag_li);
        task_list.push(task_input.value); //add task to list
        update_local_storage();
    }
});

function create_li(){
    let tag_li = document.createElement('li');

    //add checkbox  with its class to li tag;
    const checkbox_task = document.createElement('input');
    checkbox_task.setAttribute("type","checkbox");
    checkbox_task.setAttribute("class","box");
    checkbox_task.onclick=function (){
        if(this.checked){
            this.nextElementSibling.style.textDecoration = "line-through";
        }else{
            this.nextElementSibling.style.textDecoration = "none";
        }
    }
    tag_li.appendChild(checkbox_task);

    //add span with class to li tag
    const span_task = document.createElement('span');
    span_task.className += "task";
    tag_li.appendChild(span_task);

    //add delete button
    const button_delete = document.createElement('button');
    button_delete.className += "delete-btn";
    button_delete.addEventListener('click',remove_task);
    tag_li.appendChild(button_delete);
    return tag_li;
}

function update_local_storage(){
    localStorage.setItem("tasks",JSON.stringify(task_list));
}

function remove_task(){
    let task = this.parentElement.childNodes[1].textContent;
    task_list.splice(task_list.indexOf(task),1); //remove task from list
    update_local_storage();
    this.parentElement.remove();
}
