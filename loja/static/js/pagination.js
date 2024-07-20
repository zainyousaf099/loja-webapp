document.addEventListener('DOMContentLoaded', function () {
    const productCards = document.querySelectorAll('.product-card');
    const pagination = document.querySelector('.pagination');
    const pageNumbers = document.querySelectorAll('.page-num');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const itemsPerPage = 6;
    let currentPage = 1;

    function showPage(page) {
        productCards.forEach((card, index) => {
            if (index < page * itemsPerPage && index >= (page - 1) * itemsPerPage) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });

        pageNumbers.forEach((pageNum, index) => {
            if (index + 1 === page) {
                pageNum.classList.add('active');
            } else {
                pageNum.classList.remove('active');
            }
        });
    }

    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Smooth scroll to the top
        });
    }

    pageNumbers.forEach((pageNum, index) => {
        pageNum.addEventListener('click', function (e) {
            e.preventDefault();
            currentPage = index + 1;
            showPage(currentPage);
            scrollToTop(); // Scroll to top when a page number is clicked
        });
    });

    prevButton.addEventListener('click', function (e) {
        e.preventDefault();
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
            scrollToTop(); // Scroll to top when "prev" is clicked
        }
    });

    nextButton.addEventListener('click', function (e) {
        e.preventDefault();
        if (currentPage < pageNumbers.length) {
            currentPage++;
            showPage(currentPage);
            scrollToTop(); // Scroll to top when "next" is clicked
        }
    });

    showPage(currentPage);
});
