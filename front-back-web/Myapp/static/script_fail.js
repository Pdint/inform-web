
document.addEventListener("DOMContentLoaded", function () {
  // 선택한 데이터에 대한 API 호출 및 결과 표시
  document.getElementById("select").addEventListener("change", function () {
    const selectedId = this.value;
    fetchData(selectedId);
  });

  // 버튼 클릭 시에도 정보 송출
  document.getElementById("submitButton").addEventListener("click", function () {
    const selectedId = document.getElementById("select").value;
    fetchData(selectedId);
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

function fetchData(selectedId) {
  // 로컬 JSON 파일 경로
  const jsonFilePath = "C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/Myapp/static/file.json";

  // 로컬 JSON 파일을 가져옵니다.
  fetch(jsonFilePath)
    .then(response => {
      // 응답 상태가 OK인지 확인합니다.
      if (!response.ok) {
        throw new Error(`로컬 JSON 파일을 가져오는 데 실패했습니다. 상태: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      // 로컬 JSON 데이터를 처리하고 결과를 표시합니다.
      const resultData = data.find(item => item.id === parseInt(selectedId)); // 가정: JSON 배열에서 선택된 ID에 해당하는 항목 찾기
      displayResult(resultData);
    })
    .catch(error => {
      console.error("로컬 JSON 파일을 가져오는 중 오류 발생:", error);
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