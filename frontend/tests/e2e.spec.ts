import { test, expect } from '@playwright/test'

test('homepage shows title', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByText('Capstone Starter')).toBeVisible()
})
