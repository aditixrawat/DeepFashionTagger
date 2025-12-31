// preview & filename UI
const input = document.getElementById('imageInput');
const previewImg = document.getElementById('previewImg');

if (input) {
  input.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) {
      return;
    }
    // show preview locally before upload (if preview area exists)
    if (previewImg) {
      // Clean up previous object URL to prevent memory leaks
      if (previewImg.src && previewImg.src.startsWith('blob:')) {
        URL.revokeObjectURL(previewImg.src);
      }
      previewImg.src = URL.createObjectURL(file);
    }
  });
}
