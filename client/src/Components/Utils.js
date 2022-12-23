import { useState, useRef, useEffect, useCallback } from 'react';

export function timeConverter(UNIX_timestamp) {
    var t = new Date(UNIX_timestamp * 1000);
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var year = t.getFullYear();
    var month = months[t.getMonth()];
    var date = t.getDate();
    var time = date + ' ' + month + ' ' + year % 100;
    return time;
}

export function timeConverterMonthOnly(UNIX_timestamp) {
    var t = new Date(UNIX_timestamp * 1000);
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var year = t.getFullYear();
    var month = months[t.getMonth()];
    var date = t.getDate();
    var time = month + ' ' + year % 100;
    return time;
}

// export const useScrollDirection = () => {
//   const [scrollPosition, setScrollPosition] = useState(0);
//   const [isScrollingUp, setIsScrollingUp] = useState(false);
//   const [isScrollingDown, setIsScrollingDown] = useState(false);
//   const prevScrollPosition = useRef(0);

//   const handleScroll = useCallback(() => {
//     prevScrollPosition.current = scrollPosition;
//     const position = window.pageYOffset;
//     setScrollPosition(position);
//   }, [scrollPosition]);

//   useEffect(() => {
//     window.addEventListener('scroll', handleScroll, { passive: true });

//     if (scrollPosition - prevScrollPosition.current > 0) {
//       setIsScrollingUp(false);
//       setIsScrollingDown(true);
//     } else if (scrollPosition - prevScrollPosition.current < 0) {
//       setIsScrollingDown(false);
//       setIsScrollingUp(true);
//     }
//     return () => {
//       window.removeEventListener('scroll', handleScroll);
//     };
//   }, [handleScroll, scrollPosition]);

//   return { isScrollingDown, isScrollingUp };
// };
