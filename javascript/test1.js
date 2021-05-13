// 1. 자바 스크립트 타입
// var n1 = 10;
// var n2 = 10.5;
// var s1 = "문자열";
// var b1 = true;

// console.log(n1);
// console.log(n2);
// console.log(s1);
// console.log(b1);

// 2.자바스크립트 오브젝트 타입
// var board = {
//     id:1,
//     title:"제목1",
//     content:"내용1"
// };

// console.log(board);
// console.log(board.title);

// 3. 자바스크립트 함수

function add() {
    return 10;
}

var result = add();
console.log(result);

// 4. 익명함수
var m = function () {
    return 20;
};

console.log(m());

// # 5. 화살표 함수
var r = () => 20;

console.log(r());

// 6. 화살표 함수로 변경하기
var f1 = function hello(n1) {
    return n1 + 5;
}

//var f2 = (n1) => n1+5;

var f2 = (n1) => {
    n1 = n1 * 10;
    return n1 + 5;
}

console.log(f2(1));

// 7. 리스트(배열)
var arr1 = [1, 2, 3];

// for(var i=0;i<3;i++){
//     console.log(arr[i]);
// }

arr1.forEach((n) => {
    console.log(n);
});

var arr2 = arr1.map((n) => n + 5);

console.log(arr2);

// MariaDB(타임존=Asia/Seoul)=>몽고 DB(9시간 전 UTC)
// +9시간 해서 INSERT
// String타입으로 변경해서 집어넣기
// 8. Date
var today = new Date();

console.log(today);


function fx(i) {
    var r = db.users.findOne({ id: i });
    return db.users.find({ id: r.friend });
}