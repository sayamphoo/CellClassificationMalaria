const image = document.getElementById("image");
const imagePreview = document.querySelector(".image_preview img");
const submit = document.getElementById("submit");

document.addEventListener("DOMContentLoaded", () => {
  image.onchange = () => {
    const file = image.files[0];
    if (file) {
      const reader = new FileReader();

      reader.onload = (e) => {
        imagePreview.src = e.target.result;
        submit.style.backgroundColor = "#ffae00";
      };
      reader.readAsDataURL(file);
    }
  };
});

async function onSubmit(e) {
  e.preventDefault();
  const file = image.files[0];
  if (file) {
    const formData = new FormData();
    formData.append("file", file);
    try {
      const response = await fetch("/prediction", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to upload image");
      }

      const responseData = await response.json();
      
      Swal.fire({
        icon: "success",
        title: `${responseData.prediction}`,
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.reload();
        }
      });
    } catch (e) {
      console.log(e);
    }
  }
}
