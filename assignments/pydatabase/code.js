async function showCourses(id){
    const response = await fetch("/courses");
    if (response.ok)
        courses=await response.text();
    //let courses="<tr><td>1</td><td>CSCI</td><td>120</td></tr>";
    let html=`<table>
        <tr><th>Id</th><th>Class</th><th>Number</th></tr>
        ${courses}
    </table>`;
    document.getElementById(id).innerHTML=html;
}
async function addCourse(clssId,numberId){
    let clss=document.getElementById(clssId).value;
    let number=document.getElementById(numberId).value;  // $(id).value
    const url = `/add?class=${clss}&number=${number}`;
    const response = await fetch(url);
    if (response.ok)
        showCourses('courseTable');
}
async function deleteCourse(clssId,numberId){
    let clss=document.getElementById(clssId).value;
    let number=document.getElementById(numberId).value;  // $(id).value
    const url = `/del?class=${clss}&number=${number}`;
    const response = await fetch(url);
    if (response.ok)
        showCourses('courseTable');
}