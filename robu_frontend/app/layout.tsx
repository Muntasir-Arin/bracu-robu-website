import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { ThemeProvider } from "@/components/theme-provider";
import { Toaster } from "@/components/ui/sonner";
import { GoogleAnalytics, GoogleTagManager } from "@next/third-parties/google"

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Robotics Club Of Brac University",
  description:
    "The vision of Robotics Club of BRAC University (ROBU) is to realize your creative ideas through the utilization of robots. Our aim is to enhance students' understanding of global advancements in robotics. Moreover, we are committed to identifying exceptional talents in the field of Robotics and Intelligence, nurturing them, and transforming them into valuable assets for our university.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="!scroll-smooth">
      <GoogleTagManager gtmId="GTM-W49HDCP9" />
      <body className={inter.className}>
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
          {children}
          <Toaster closeButton />
        </ThemeProvider>
      </body>
      <GoogleAnalytics gaId="G-NSSY6GCGJX" />
    </html>
  );
}
