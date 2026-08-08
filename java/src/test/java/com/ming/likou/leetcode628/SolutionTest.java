package com.ming.likou.leetcode628;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolutionTest {

    private final Solution solution = new Solution();

    @Test
    void allPositive() {
        assertEquals(6, solution.maximumProduct(new int[]{1, 2, 3}));
    }

    @Test
    void allNegative() {
        assertEquals(-6, solution.maximumProduct(new int[]{-1, -2, -3}));
    }

    @Test
    void mixedWithTwoNegatives() {
        // -10 * -10 * 5 = 500, 比 1 * 2 * 5 = 10 大
        assertEquals(500, solution.maximumProduct(new int[]{-10, -10, 1, 2, 5}));
    }

    @Test
    void mixedWithOneNegative() {
        // 排序后 {-5, 1, 2, 3, 4}，最大乘积 = 4 * 3 * 2 = 24
        assertEquals(24, solution.maximumProduct(new int[]{-5, 1, 4, 3, 2}));
    }
}
