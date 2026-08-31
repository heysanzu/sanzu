 /* ── CHANGELOG POPUP ── */
    function openPopup() {
      document.getElementById('overlay').classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function closePopup() {
      document.getElementById('overlay').classList.remove('open');
      document.body.style.overflow = '';
    }
    function closePopupOnOverlay(e) {
      if (e.target === document.getElementById('overlay')) closePopup();
    }
    function closeBanner(e) {
      e.stopPropagation();
      document.getElementById('newsBanner').style.display = 'none';
    }

    /* ── UPCOMING POPUP ── */
    function openUpcoming() {
      document.getElementById('upcomingOverlay').classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function closeUpcoming() {
      document.getElementById('upcomingOverlay').classList.remove('open');
      document.body.style.overflow = '';
    }
    function closeUpcomingOnOverlay(e) {
      if (e.target === document.getElementById('upcomingOverlay')) closeUpcoming();
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closePopup();
        closeUpcoming();
      }
    });

    /* ── SCREENSHOT CAROUSEL AUTO-SCROLL ── */
    (function () {
      const overflow = document.getElementById('screenshotsOverflow');
      const track    = document.getElementById('screenshotsTrack');
      if (!overflow || !track) return;

      const frames     = track.querySelectorAll('.screenshot-frame');
      const total      = frames.length;
      let current      = 0;
      let userPaused   = false;
      let timer        = null;

      function getFrameW() {
        return frames[0].offsetWidth + 16; /* gap 1rem ≈ 16px */
      }

      function goTo(idx) {
        /* wrap around */
        if (idx >= total) idx = 0;
        if (idx < 0)      idx = total - 1;
        current = idx;
        overflow.scrollTo({ left: current * getFrameW(), behavior: 'smooth' });
      }

      function startAuto() {
        clearInterval(timer);
        timer = setInterval(() => {
          if (!userPaused) goTo(current + 1);
        }, 2500);
      }

      /* sync current on manual swipe */
      overflow.addEventListener('scroll', () => {
        current = Math.round(overflow.scrollLeft / getFrameW());
      }, { passive: true });

      /* pause while user interacts */
      overflow.addEventListener('mouseenter', () => { userPaused = true; });
      overflow.addEventListener('mouseleave', () => { userPaused = false; });
      overflow.addEventListener('touchstart', () => { userPaused = true; }, { passive: true });
      overflow.addEventListener('touchend',   () => { setTimeout(() => { userPaused = false; }, 2000); }, { passive: true });

      startAuto();
    })();

    /* ── REVIEWS AUTO-SLIDE + DOTS ── */
    (function () {
      const rail  = document.getElementById('reviewsRail');
      const dots  = document.querySelectorAll('#reviewsDots span');
      if (!rail || !dots.length) return;

      const cards   = rail.querySelectorAll('.review-card');
      const total   = cards.length;
      let current   = 0;
      let timer     = null;
      let userPaused = false;

      function getCardW() {
        return cards[0].offsetWidth + Math.round(parseFloat(getComputedStyle(rail).gap) || 14);
      }

      function goTo(idx) {
        current = (idx + total) % total;
        rail.scrollTo({ left: current * getCardW(), behavior: 'smooth' });
        dots.forEach((d, i) => d.classList.toggle('active', i === current));
      }

      function startAuto() {
        clearInterval(timer);
        timer = setInterval(() => {
          if (!userPaused) goTo(current + 1);
        }, 3000);
      }

      /* sync dots on manual swipe */
      rail.addEventListener('scroll', () => {
        const idx = Math.round(rail.scrollLeft / getCardW());
        dots.forEach((d, i) => d.classList.toggle('active', i === idx));
        current = idx;
      }, { passive: true });

      /* pause auto-slide while user interacts */
      rail.addEventListener('touchstart', () => { userPaused = true; }, { passive: true });
      rail.addEventListener('touchend',   () => { setTimeout(() => { userPaused = false; }, 2000); }, { passive: true });
      rail.addEventListener('mouseenter', () => { userPaused = true; });
      rail.addEventListener('mouseleave', () => { userPaused = false; });

      startAuto();
    })();

    /* ── FAQ ── */
    function toggleFaq(btn) {
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      // close all
      document.querySelectorAll('.faq-q').forEach(b => {
        b.setAttribute('aria-expanded', 'false');
        b.nextElementSibling.classList.remove('open');
      });
      // open clicked if it was closed
      if (!expanded) {
        btn.setAttribute('aria-expanded', 'true');
        btn.nextElementSibling.classList.add('open');
      }
    }
