/*
document.getElementById("submitButton").addEventListener("click", function () {
  document.getElementById("userInfo")
  //var html_output_from_django = JSON.parse(document.getElementById('html_output').textContent);
  var html_output_from_django = JSON.parse("{{ data|escapejs }}");
  console.log(html_output_from_django);
  document.getElementById("userInfo").innerHTML = html_output_from_django;
});
*/

/*
var clickcount = 0;
document.getElementById("submitButton").addEventListener("click", function () {
  var htmlElement = document.getElementById("pd_data");
  var variableValue = htmlElement.getAttribute("data");
  clickcount++

  if (clickcount % 2 === 1) 
  {
   // 홀수 번째 클릭일 때
    document.getElementById("userInfo").innerHTML = variableValue;
  }
  else 
  {
    // 짝수 번째 클릭일 때
    document.getElementById("userInfo").innerHTML = "";
  }
})
*/



// 출력 버튼 클릭 시 내용 출력 or 숨김 용도
var clickcount = 0;

// Id가 submitButton인 값을 클릭 했을 때 Id가 pd_data인 값 안에 있는 data라는 변수(?)를 variableValue에 넣음
document.getElementById("submitButton").addEventListener("click", function () {
  var htmlElement = document.getElementById("pd_data");
  var variableValue_part = htmlElement.getAttribute("data_pd_part");
  var variableValue_all = htmlElement.getAttribute("data_all");
  clickcount++;

  //Id가 select인 값 중에 선택된 옵션(블루 아카이브 or 전체)에 대응하는 value 값을 selectedValue에 넣음
  var selectElement = document.getElementById("select");
  var selectedValue = selectElement.options[selectElement.selectedIndex].value;

  if (selectedValue === "1") 
  {
    // 선택한 값이 1인 경우(블루 아카이브 value일 경우) 내용 출력
    document.getElementById("userInfo").innerHTML = variableValue_part; 
  } 
  else if (selectedValue === "2") 
  {
    // 선택한 값이 2인 경우(전체 value일 경우) 내용 출력
    document.getElementById("userInfo").innerHTML = variableValue_all;
  }

  if (clickcount % 2 === 0) {
    // 짝수 번째 클릭시에 내용 숨김
    document.getElementById("userInfo").innerHTML = "";
  }
});

//  select중 value값이 변경될 때마다 감지
document.getElementById("select").addEventListener("change", function () {
  // 출력값 초기화
  document.getElementById("userInfo").innerHTML = "";
});


/*
function getData() {
  return JSON.parse(document.getElementById('jsonData').value);
}

var displayButton = document.getElementById('submitButton');
displayButton.addEventListener('click', function () {
  // JSON 데이터를 가져와서 사용
  var jsonData = getData();
  try {
      JSON.parse(jsonData);
  } catch (error) {
     console.error('Error parsing JSON:', error);
  }
  
  // 여기서 jsonData를 활용하여 필요한 동작을 수행
  var jsonString = JSON.stringify(jsonData, null, 2);

  // 데이터프레임 HTML을 출력하는 부분
  var dataFrameOutput = document.getElementById("dataFrameOutput");
  //dataFrameOutput.textContent = jsonString;
  dataFrameOutput.innerHTML = jsonString;
});
*/


/*
document.addEventListener("DOMContentLoaded", function () {
    // 선택한 데이터에 대한 API 호출 및 결과 표시
    document.getElementById("select").addEventListener("change", function () {
      const selectedValue = this.value;
      //fetchData(selectedValue);
    });
  
    // 버튼 클릭 시에도 정보 송출
    document.getElementById("submitButton").addEventListener("click", function () {
      document.getElementById('userInfo')
      htmlOutput = 12345
      document.getElementById("userInfo").innerHTML = htmlOutput;
    });

  
    // document 클릭 시 결과 영역 숨김
    document.addEventListener("click", function (event) {
      const resultDiv = document.getElementById("result");
  
      // 클릭된 요소가 결과 영역이나 관련 요소인지 확인
      if (!resultDiv.contains(event.target) && event.target.id !== "select" && event.target.id !== "submitButton") {
        // 결과 영역 숨기기
        resultDiv.style.display = "none";
      }
    });
  });

 
  function fetchData() {
    var djangoData = document.getElementById('userInfo').getAttribute('data-django-variable');
    console.log(djangoData);
    ("submitButton").click(function() {
      var htmlOutput = df.toHtml();
      ("userInfo").html(htmlOutput);
    });
  } 


  
  function displayResult(data) {
    // 이미지를 표시할 img 요소
    const userImage = document.getElementById("userImage");
    // 결과를 표시할 div
    const userInfoDiv = document.getElementById("userInfo");
    // 결과를 표시할 div
    const resultDiv = document.getElementById("result");
  
    // 이전에 표시된 내용 지우기
    userInfoDiv.innerHTML = "";
  
    // 이미지 URL이 있다면 이미지 표시
    if (data.hasOwnProperty("image")) {
      userImage.src = data.image;
      userImage.style.display = "block";
    } else {
      userImage.style.display = "none";
    }
  
    // 결과를 텍스트로 변환하여 표시
    for (const key in data) {
      if (data.hasOwnProperty(key) && key !== "image") {
        const paragraph = document.createElement("p");
        paragraph.innerHTML = `<strong>${key}:</strong> ${data[key]}`;
        userInfoDiv.appendChild(paragraph);
      }
    }
  
    // 결과 영역 보이기
    resultDiv.style.display = "block";
  }
  */